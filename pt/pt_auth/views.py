from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from .forms import CustomUserCreationForm, DonorPaymentForm, CreateDonorForm
from .models import *
from itertools import chain
from django.db import connection
from django.contrib import messages


# Create your views here.


def register_view(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'pt_auth/register.html', context)


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('passwd')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user=user)
            return redirect('home')
        else:
            return redirect('')
    return render(request, 'pt_auth/login.html')


def logOutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home_view(request):
    username = request.user.username
    email = request.user.email
    member = Member.objects.get(username=username)
    id = member.m_id
    head = Head.objects.all()
    subhead = SubHead.objects.all()
    vol = Volunteer.objects.all()
    if request.user.is_superuser:
        return redirect('super')
    for i in range(len(head)):
        print(head[i].head.m_id)
        if id == head[i].head.m_id:
            return redirect('head')
    for i in range(len(subhead)):
        print(subhead[i].sub_head.m_id)
        if id == subhead[i].sub_head.m_id:
            return redirect('subhead')
    for i in range(len(vol)):
        print(vol[i].volunteer.m_id)
        if id == vol[i].volunteer.m_id:
            return redirect('vol')

    return render(request, 'pt_auth/home.html')


@login_required(login_url='login')
def head_view(request):
    username = request.user.username
    print(username)
    member = Member.objects.get(username=username)
    id = member.m_id
    subhead = SubHead.objects.filter(head_id=id).all()
    subhead_len = len(subhead)
    # donor_payments = Payments.objects.get()
    vol_list = []
    for i in range(subhead_len):
        vol_list.append(i)
    for v in range(0, subhead_len):
        vol_list[v] = VolunteerAssignment.objects.filter(sub_head=subhead[v].sub_head.m_id).all()
    for v in vol_list:
        for i in v:
            print(i.volunteer.volunteer.m_id)
    donor = Donor.objects.all().order_by('donor_id')
    donor_len = len(donor)
    payments = Payments.objects.all().order_by('donor_id')
    print(payments)
    donor_payments = zip(donor, payments)

    context = dict(subhead=subhead, vol=vol_list, donor_payments=donor_payments, donor_len=donor_len)
    return render(request, 'pt_auth/head.html', context)


@login_required(login_url='login')
def subhead_view(request):
    username = request.user.username
    member = Member.objects.get(username=username)
    id = member.m_id
    vol = Volunteer.objects.filter(sub_head=id).all()
    print(vol)
    donor_list = []
    for i in range(len(vol)):
        donor_list.append(i)
    for d in range(0, len(vol)):
        donor_list[d] = DonorAssignment.objects.filter(volunteer=vol[d].volunteer.m_id).all().order_by('donor_id')
    flatten_donor_list = list(chain.from_iterable(donor_list))
    print(flatten_donor_list[0])
    donor_payment_list = []
    for d in donor_list:
        for i in d:
            donor_payment_list.append(i)
    z = 0
    for d in donor_list:
        for i in d:
            donor_payment_list[z] = Collection.objects.filter(donor_id=i.donor.donor_id).all().order_by('donor_id')
            z = z + 1
    flatten_donor_payments_list = list(chain.from_iterable(donor_payment_list))
    donor_payments = zip(flatten_donor_payments_list, flatten_donor_list)
    context = dict(vol=vol, donor_payment=zip(flatten_donor_payments_list, flatten_donor_list),
                   donor=flatten_donor_list)
    return render(request, 'pt_auth/subhead.html', context)


@login_required(login_url='login')
def donor_payment_form_view(request, pk_d):
    donor = Collection.objects.get(donor_id=pk_d)
    form = DonorPaymentForm(initial={'donor': donor.donor_id, 'payment': donor.payment,
                                     'payment_month': donor.payment_month, 'volunteer': donor.volunteer})
    if request.method == 'POST':
        form = DonorPaymentForm(request.POST, instance=donor)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'pt_auth/Donor_payment_form.html', context)


@login_required(login_url='login')
def volunteer_view(request):
    uname = request.user.username
    member = Member.objects.get(username=uname)
    vol = Volunteer.objects.get(volunteer=member.m_id)
    donor_ass = DonorAssignment.objects.filter(volunteer=vol).all().order_by('donor_id')
    donor_list = []
    print(donor_ass)
    try:
        d_len = len(donor_ass)
    except:
        d_len = 1

    print(d_len)
    for i in range(d_len):
        donor_list.append(i)
    z = 0
    for i in donor_ass:
        donor_list[z] = Donor.objects.get(donor_id=i.donor_id)
        z = z + 1
    print(donor_list)
    donation_list = []
    for i in range(z):
        donation_list.append(i)
    p = 0
    for i in donor_list:
        donation_list[p] = Collection.objects.filter(donor=i)
    flatten_donation_list = list(chain.from_iterable(donation_list))
    donor_payments = zip(donor_list, flatten_donation_list)
    context = {'donor_payments': donor_payments}
    return render(request, 'pt_auth/volunteer.html', context)


@login_required(login_url='login')
@permission_required('is_superuser')
def admin_view(request):
    head = Head.objects.all()
    subhead = SubHead.objects.all()
    vol = Volunteer.objects.all()
    donor = Donor.objects.all().order_by('donor_id')
    payments = Collection.objects.all().order_by('donor_id')
    donor_payments = zip(donor, payments)
    context = {'head': head,
               'subhead': subhead,
               'vol': vol,
               'donor_payments': donor_payments,
               }
    return render(request, 'pt_auth/auth.html', context)


@login_required(login_url='login')
def delete_donor(request, pk):
        cursor = connection.cursor()
        donor_id = 3
        # with connection.cursor() as cursor:
        #     cursor.execute("DELETE donor_id,name,phone_no,email,team_id FROM donor WHERE donor_id=11")
        return redirect('home')

def create_donor_view(request):
    form = CreateDonorForm
    if request.method == 'POST':
        name = request.POST.get('name')
        id= request.POST.get('id')
        email = request.POST.get('email')
        phone_no = request.POST.get('contact_no')
        team = request.POST.get('department')
        team_id = 0
        if team == 'Mess Bill Aid':
            team_id = 1
        else:
            team_id = 2
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO donor(Donor_ID, Name, Phone_No, D_Email, Team_ID)  VALUES (%s,%s,%s,%s,%s)",[id,name,phone_no,email,team_id])
    return render(request, 'pt_auth/create_donor.html')

def index_view(request):
    return render(request,'pt_auth/index.html')