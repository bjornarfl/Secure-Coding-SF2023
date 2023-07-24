from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import datetime
from .models import PaymentInfo, Station, BikeRental, SubscriptionType, CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm, SubscriptionUpdateForm, PaymentInfoCreationForm

#frontpage
def home(request):
    context = {
        'subscriptions': SubscriptionType.objects.all(),
        'stationcount': Station.objects.all().count(),
    }
    return render(request, "BaaS/home.html", context)

#Create a new account
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, "BaaS/register.html", {'form': form})

@login_required
def profile(request, pk):
    user = CustomUser.objects.filter(pk=pk).first()
    if request.method == 'POST':
        u_form = CustomUserChangeForm(request.POST, instance=user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Profile has been updated!')
            return redirect('baas-profile', pk=user.pk)
    else:
        u_form = CustomUserChangeForm(instance=user)
    
    rentals = BikeRental.objects.filter(user=user).order_by('-start_time')
    if request.GET.get('search'):
        rentals = rentals.filter(Q(start_station__address__icontains=request.GET.get('search')) | Q(end_station__address__icontains=request.GET.get('search')))
    if request.GET.get('id'):
        query = f"SELECT * FROM BaaS_bikerental WHERE BaaS_bikerental.id LIKE '%{request.GET.get('id')}%'"
        rentals = rentals.raw(query)
    stations = Station.objects.all()

    context = {
        'user': user,
        'u_form': u_form,
        'rentals': rentals,
        'stations': stations,
    }
    return render(request, "BaaS/profile.html", context)

@login_required
def updateSubscription(request):
    if request.method == 'POST' and hasattr(request.user, 'subscription'): #Change existing subscription
        form = SubscriptionUpdateForm(request.POST, instance=request.user.subscription)
        if form.is_valid():
            sub = form.save(commit=False)
            if sub.subscriptiontype == request.user.subscription.subscriptiontype and request.user.subscription.is_valid():
                #if subscription type did not change, keep the old start time
                sub.start_time = request.user.subscription.start_time
            else:
                sub.start_time = datetime.date.today()
            sub.user = request.user
            sub.save()
            messages.success(request, "Subscription was updated!")
            return redirect("baas-profile", pk=request.user.pk)
    elif request.method == 'POST': #Create new subscription
        form = SubscriptionUpdateForm(request.POST)
        if form.is_valid():
            sub = form.save(commit=False)
            sub.start_time = datetime.date.today()
            sub.user = request.user
            sub.save()
            messages.success(request, "Subscription was created!")
            return redirect("baas-profile", pk=request.user.pk)
    elif hasattr(request.user, 'subscription'):
        form = SubscriptionUpdateForm(instance=request.user.subscription)
    else:
        form = SubscriptionUpdateForm()
    context = {
        'subscriptions': SubscriptionType.objects.all(),
        'paymentinfo': PaymentInfo.objects.filter(user=request.user),
        'form': form
    }
    return render(request, "BaaS/subscription.html", context)

@login_required
def paymentInfo(request):
    if request.method == 'POST':
        form = PaymentInfoCreationForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.user = request.user
            p.save()
            messages.success(request, "Paymentinfo was added!")
            return redirect('baas-payment')
    else:
        form = PaymentInfoCreationForm()
    context = {
        'paymentinfo': PaymentInfo.objects.filter(user=request.user),
        'form': form
    }
    return render(request, "BaaS/paymentinfo.html", context)

@login_required
def deletePaymentInfo(request, pk):
    paymentinfo = PaymentInfo.objects.filter(pk=pk, user=request.user).first()
    if paymentinfo:
        paymentinfo.delete()
        messages.info(request, "Paymentinfo was deleted")
    else:
        messages.error(request, "Something went wrong, please try again")
    return redirect('baas-payment')