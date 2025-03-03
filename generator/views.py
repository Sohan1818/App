import random
import string

from django.shortcuts import render

def generate_password(length=8, use_letters=True, use_numbers=False, use_special=False):
    char_pool = ''
    if use_letters:
        char_pool += string.ascii_letters
    if use_numbers:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation
    
    if not char_pool:
        char_pool = string.ascii_letters  # Default to letters if nothing is selected
    
    return ''.join(random.choice(char_pool) for _ in range(length))

def home(request):
    password = ''
    if request.method == "POST":
        length = int(request.POST.get("length", 8))
        use_letters = "letters" in request.POST
        use_numbers = "numbers" in request.POST
        use_special = "special" in request.POST
        
        password = generate_password(length, use_letters, use_numbers, use_special)
    
    return render(request, "index.html", {"password": password})