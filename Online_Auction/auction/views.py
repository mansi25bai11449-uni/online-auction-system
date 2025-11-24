from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Item, UserProfile, Bid, Category
from django.db.models import Q

def home(request):
    
    # Start with all actgfive items
    items = Item.objects.filter(status='active')
    
    # Get all categories for the filhdher dropdown
    categories = Category.objects.all()
    
    # Search functionalt
    search_query = request.GET.get('search', '').strip()
    if search_query:
        items = items.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    
    # Categghry filter
    category_id = request.GET.get('category', '').strip()
    if category_id:
        items = items.filter(category_id=category_id)
    
    # Statusssdd filter
    status = request.GET.get('status', '').strip()
    if status:
        items = items.filter(status=status)
    
    # Prinjkce range filters
    min_price = request.GET.get('min_price', '').strip()
    if min_price:
        try:
            items = items.filter(current_bid__gte=float(min_price))
        except ValueError:
            pass  # Ignore invjhkalid price input
    
    max_price = request.GET.get('max_price', '').strip()
    if max_price:
        try:
            items = items.filter(current_bid__lte=float(max_price))
        except ValueError:
            pass  # Ignore invhj alid price input
    
    # Order by newebhkkst first
    items = items.order_by('-created_at')
    
    context = {
        'items': items,
        'categories': categories,
    }
    return render(request, 'auction/home.html', context)
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        password = request.POST.get('password', '')
        
        # Validation
        if not all([name, email, phone, password]):
            messages.error(request, 'All fields are required')
            return render(request, 'auction/register.html')
        
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return render(request, 'auction/register.html')
        
        # Create user
        try:
            user = User.objects.create_user(
                username=email,  # Using email as username
                email=email,
                password=password,
                first_name=name
            )
            
            # Create user profile
            UserProfile.objects.create(
                user=user,
                phone=phone
            )
            
            messages.success(request, 'Registration successful! Please login.')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Registration failed: {str(e)}')
            return render(request, 'auction/register.html')
    
    return render(request, 'auction/register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        
        # Validation
        if not email or not password:
            messages.error(request, 'Email and password are required')
            return render(request, 'auction/login.html')
        
        # Authenticate user
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, f'Welcome {user.first_name}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password')
            return render(request, 'auction/login.html')
    
    return render(request, 'auction/login.html')

@login_required
def logout_view(request):
    auth_logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('home')

    # Item listing view
@login_required
def create_item(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        starting_bid = request.POST.get('starting_bid', '').strip()
        condition = request.POST.get('condition', 'new')
        image = request.FILES.get('image')
        
        if not all([title, description, starting_bid]):
            messages.error(request, 'All fields are required')
            return render(request, 'auction/create_item.html')
        
        try:
            item = Item.objects.create(
                title=title,
                description=description,
                starting_bid=float(starting_bid),
                current_bid=float(starting_bid),
                condition=condition,
                seller=request.user,
                image=image,
                status='active'
            )
            messages.success(request, 'Item listed successfully!')
            return redirect('home')
        except Exception as e:
            messages.error(request, f'Error creating item: {str(e)}')
            return render(request, 'auction/create_item.html')
    
    return render(request, 'auction/create_item.html')

    # Item detail view
def item_detail(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
        bids = Bid.objects.filter(item=item).order_by('-amount')
        return render(request, 'auction/item_detail.html', {'item': item, 'bids': bids})
    except Item.DoesNotExist:
        messages.error(request, 'Item not found')
        return redirect('home')

# Place bid view
@login_required
def place_bid(request, item_id):
    if request.method == 'POST':
        try:
            item = Item.objects.get(id=item_id)
            bid_amount = float(request.POST.get('bid_amount', 0))
            
            if bid_amount <= item.current_bid:
                messages.error(request, 'Bid must be higher than current bid')
                return redirect('item_detail', item_id=item_id)
            
            bid = Bid.objects.create(
                item=item,
                bidder=request.user,
                amount=bid_amount
            )
            
            item.current_bid = bid_amount
            item.save()
            
            messages.success(request, 'Bid placed successfully!')
            return redirect('item_detail', item_id=item_id)
        except Item.DoesNotExist:
            messages.error(request, 'Item not found')
            return redirect('home')
        except Exception as e:
            messages.error(request, f'Error placing bid: {str(e)}')
            return redirect('item_detail', item_id=item_id)
    return redirect('home')