from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Supplier, Tender, ProductRate
from .forms import TenderForm
from django.contrib.auth.hashers import check_password

# Supplier Dashboard View
def dashboard(request):
    supplier_id = request.session.get('supplier_id')
    if not supplier_id:
        return redirect('supplier_login')  # Redirect to login if not authenticated
    
    supplier = get_object_or_404(Supplier, supplier_id=supplier_id)
    last_order = supplier.tenders.filter(status="Accepted").order_by('-id').first()
    product_rates = ProductRate.objects.all()

    return render(request, 'fmcg/dashboard.html', {
        'supplier': supplier,
        'last_order': last_order,
        'product_rates': product_rates,
    })

# Submit Tender View
def submit_tender(request):
    supplier_id = request.session.get('supplier_id')
    if not supplier_id:
        return redirect('supplier_login')

    supplier = Supplier.objects.get(supplier_id=supplier_id)

    if request.method == 'POST':
        form = TenderForm(request.POST)
        if form.is_valid():
            tender = form.save(commit=False)
            tender.supplier = supplier
            tender.status = 'Pending'  # Default status for new tenders
            tender.save()
            messages.success(request, "Tender submitted successfully!")
            return redirect('supplier_dashboard')
        else:
            messages.error(request, "Failed to submit tender. Please check the form.")
    
    form = TenderForm()
    return render(request, 'fmcg/submit_tender.html', {'form': form})

# Supplier Login View
def supplier_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            supplier = Supplier.objects.get(username=username)
            if check_password(password, supplier.password):
                request.session['supplier_id'] = supplier.supplier_id
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid password.")
        except Supplier.DoesNotExist:
            messages.error(request, "Invalid username.")
    
    return render(request, 'fmcg/login.html')

def track_progress(request):
    supplier_id = request.session.get('supplier_id')
    if not supplier_id:
        return redirect('supplier_login')

    supplier = Supplier.objects.get(supplier_id=supplier_id)
    last_tender = supplier.tenders.order_by('-id').first()  # Get the latest tender

    return render(request, 'fmcg/track_progress.html', {'last_tender': last_tender})

def vendor_login(request):
    return render(request, 'fmcg/vendor_login.html')
