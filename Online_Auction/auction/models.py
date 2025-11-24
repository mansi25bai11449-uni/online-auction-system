from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	
	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name_plural = 'Categories'

class Item(models.Model):
	STATUS_CHOICES = [
		('active', 'Active'),
		('closed', 'Closed'),
		('sold', 'Sold'),
	]
	
	CONDITION_CHOICES = [
		('new', 'New'),
		('used', 'Used'),
		('refurbished', 'Refurbished'),
	]
	
	title = models.CharField(max_length=200)
	description = models.TextField()
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
	condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='used')
	seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items_selling')
	starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
	current_bid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	image_url = models.URLField(max_length=500, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	end_date = models.DateTimeField()
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
	
	def __str__(self):
		return self.title
	
	class Meta:
		ordering = ['-created_at']

class Bid(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='bids')
	bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids_made')
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	timestamp = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return f'{self.bidder.username} - ${self.amount} on {self.item.title}'
	
	class Meta:
		ordering = ['-timestamp']

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	bio = models.TextField(blank=True)
	phone = models.CharField(max_length=20, blank=True)
	address = models.TextField(blank=True)
	
	def __str__(self):
		return f"{self.user.username}'s Profile"

class Watchlist(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watchlist')
	item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='watchers')
	added_at = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return f"{self.user.username} watching {self.item.title}"
	
	class Meta:
		unique_together = ['user', 'item']