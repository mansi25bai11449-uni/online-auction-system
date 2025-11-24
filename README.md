
# 🏆 Online Auction System

A full-featured web-based auction platform built with Django that allows users to list items, place bids, and manage auctions in real-time.

![Online Auction Homepage](https://images.unsplash.com/photo-1573164713712-03790a178651?w=800)

## 📋 Overview

The Online Auction System is a comprehensive e-commerce platform that enables users to:
- Browse and search through various auction items with advanced filtering
- Place bids on items they're interested in
- List their own items for auction
- Track bidding history and manage their listings
- View detailed item information with images

## ✨ Features

### Core Functionality
- **User Authentication**: Secure registration, login, and profile management
- **Item Listing**: Create auction listings with title, description, category, starting bid, and images
- **Real-time Bidding**: Place bids on active auctions with validation
- **Advanced Search & Filters**:
  - Search by title or description
  - Filter by category
  - Filter by status (active/closed/sold)
  - Price range filtering (min/max)
- **Item Images**: Display product images from external URLs
- **Watchlist**: Save favorite items for quick access
- **User Dashboards**:
  - Seller dashboard to manage listings
  - Buyer dashboard to track bids
- **Categories**: Organize items into different categories
- **Bid History**: View all bids placed on items

### Additional Features
- Responsive design for mobile and desktop
- Clean and modern UI with gradient backgrounds
- Status badges (Active/Closed/Sold)
- Seller information display
- End date tracking for auctions

## 🛠️ Technologies Used

### Backend
- **Python 3.9+**: Core programming language
- **Django 4.x**: Web framework
- **SQLite**: Database (development)
- **Django ORM**: Database abstraction layer

### Frontend
- **HTML5**: Markup
- **CSS3**: Styling with modern gradients and animations
- **JavaScript**: Dynamic functionality
- **Bootstrap/Tailwind**: Responsive design framework

### Additional Tools
- **Git**: Version control
- **GitHub Codespaces**: Development environment
- **Unsplash API**: Product images

## 📦 Installation

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)
- Git

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/online-auction.git
cd online-auction/Online_Auction
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist, install Django manually:
```bash
pip install django
```

### Step 4: Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
```
Follow the prompts to create your admin account.

### Step 6: Run Development Server
```bash
python manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000/`

### Step 7: Access Admin Panel
Visit `http://127.0.0.1:8000/admin/` and login with your superuser credentials to manage the application.

## 📂 Project Structure

```
online-auction/
├── Online_Auction/          # Django project folder
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py         # Project settings
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py
├── auction/                 # Main auction app
│   ├── migrations/         # Database migrations
│   ├── templates/          # HTML templates
│   │   └── auction/
│   │       ├── base.html   # Base template
│   │       ├── home.html   # Homepage
│   │       └── applybid.html
│   ├── __init__.py
│   ├── admin.py           # Admin configuration
│   ├── apps.py            # App configuration
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── urls.py            # App URL patterns
│   └── tests.py           # Unit tests
├── db.sqlite3             # SQLite database
├── manage.py              # Django management script
└── README.md              # This file
```

## 🗄️ Database Models

### Category
- Name
- Description

### Item
- Title
- Description
- Category (Foreign Key)
- Seller (Foreign Key to User)
- Starting Bid
- Current Bid
- Image URL
- Created At
- End Date
- Status (active/closed/sold)

### Bid
- Item (Foreign Key)
- Bidder (Foreign Key to User)
- Amount
- Timestamp

### UserProfile
- User (One-to-One with Django User)
- Bio
- Phone
- Address

### Watchlist
- User (Foreign Key)
- Item (Foreign Key)
- Added At


## 🚀 Usage

### For Buyers
1. **Browse Items**: Visit the homepage to see all active auctions
2. **Search & Filter**: Use the search bar and filters to find specific items
3. **View Details**: Click on any item to see full details
4. **Place Bid**: Enter your bid amount (must be higher than current bid)
5. **Track Bids**: View your bidding history in your dashboard
6. **Add to Watchlist**: Save items you're interested in

### For Sellers
1. **Create Listing**: Click "Create Item" and fill in the details
2. **Add Images**: Provide image URLs for your items
3. **Set Parameters**: Choose category, starting bid, and end date
4. **Manage Listings**: View and edit your active listings
5. **Track Bids**: Monitor bids received on your items
6. **Close Auctions**: Mark items as sold when auction ends

## 🔧 Configuration

### Settings
Edit `Online_Auction/settings.py` for:
- Database configuration
- Static files settings
- Media files configuration
- Security settings

### Environment Variables (Recommended for Production)
```bash
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
DATABASE_URL=postgresql://...
```

## 🧪 Running Tests

```bash
python manage.py test auction
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Django Documentation
- Bootstrap/Tailwind CSS
- Unsplash for product images
- Stack Overflow community

## 📞 Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**Made with ❤️ using Django**