# How to Add Your Own Pickup Lines 💕

There are several ways to add your own pickup lines to the application:

## Method 1: Using Django Admin (Recommended) 🎯

1. **Create a superuser account:**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create your admin account.

2. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

3. **Access the admin panel:**
   - Go to `http://127.0.0.1:8000/admin/`
   - Login with your superuser credentials
   - Click on "Pickup lines" under the "PICKUP_LINES" section
   - Click "Add Pickup line" to add new ones
   - Fill in the form:
     - **Text**: Your pickup line
     - **Category**: Choose "romantic" or "techy"
   - Click "Save"

## Method 2: Using Django Shell 🐍

1. **Open Django shell:**
   ```bash
   python manage.py shell
   ```

2. **Add pickup lines programmatically:**
   ```python
   from pickup_lines.models import PickupLine
   
   # Add romantic pickup lines
   PickupLine.objects.create(
       text="Your romantic pickup line here",
       category="romantic"
   )
   
   # Add techy pickup lines
   PickupLine.objects.create(
       text="Your techy pickup line here",
       category="techy"
   )
   
   # Add multiple at once
   romantic_lines = [
       "Are you a WiFi signal? Because I'm feeling a strong connection.",
       "Is your name Google? Because you have everything I've been searching for.",
       "Do you have a map? I keep getting lost in your eyes."
   ]
   
   for line in romantic_lines:
       PickupLine.objects.create(text=line, category="romantic")
   ```

## Method 3: Modify the Management Command 📝

1. **Edit the file:** `pickup_lines/management/commands/populate_pickup_lines.py`

2. **Add your pickup lines to the lists:**
   ```python
   # Add to romantic_lines list
   romantic_lines = [
       "Your existing lines...",
       "Your new romantic pickup line here",
       "Another romantic pickup line",
   ]
   
   # Add to techy_lines list
   techy_lines = [
       "Your existing lines...",
       "Your new techy pickup line here",
       "Another techy pickup line",
   ]
   ```

3. **Run the command to populate:**
   ```bash
   python manage.py populate_pickup_lines
   ```
   ⚠️ **Warning:** This will delete all existing pickup lines and replace them with the ones in the command.

## Method 4: Direct Database Access 🗄️

If you're comfortable with SQL, you can directly insert into the database:

```sql
INSERT INTO pickup_lines_pickupline (text, category, created_at) 
VALUES ('Your pickup line here', 'romantic', datetime('now'));
```

## Tips for Great Pickup Lines 💡

### Romantic Pickup Lines:
- Use metaphors and comparisons
- Be sweet and charming
- Keep them light and fun
- Examples: "Are you a magician? Because whenever I look at you, everyone else disappears."

### Techy + Romantic Pickup Lines:
- Combine programming/tech terms with romance
- Use tech metaphors for love
- Be creative with technical concepts
- Examples: "Are you a computer? Because you're running through my mind all the time."

## Managing Your Pickup Lines 📊

- **View all pickup lines:** Use Django admin or shell
- **Edit existing lines:** Use Django admin
- **Delete pickup lines:** Use Django admin
- **Count pickup lines:** 
  ```python
  from pickup_lines.models import PickupLine
  print(f"Romantic: {PickupLine.objects.filter(category='romantic').count()}")
  print(f"Techy: {PickupLine.objects.filter(category='techy').count()}")
  ```

## Adding Background Music 🎵

To add "Perfect" by Ed Sheeran or any other music:

1. **Create a static directory for music:**
   ```bash
   mkdir pickup_lines/static
   mkdir pickup_lines/static/music
   ```

2. **Add your music file:**
   - Place your music file (e.g., `perfect.mp3`) in `pickup_lines/static/music/`
   - The template is already configured to look for `/static/music/perfect.mp3`

3. **Update settings.py to serve static files:**
   ```python
   STATIC_URL = '/static/'
   STATICFILES_DIRS = [
       BASE_DIR / "pickup_lines" / "static",
   ]
   ```

4. **Update the audio source in the template:**
   ```html
   <source src="/static/music/perfect.mp3" type="audio/mpeg">
   ```

## Quick Start Commands 🚀

```bash
# Navigate to project directory
cd pickup_lines_app

# Create superuser (for admin access)
python manage.py createsuperuser

# Start the server
python manage.py runserver

# Access the app
# http://127.0.0.1:8000/

# Access admin panel
# http://127.0.0.1:8000/admin/
```

Happy adding pickup lines! 💕✨
