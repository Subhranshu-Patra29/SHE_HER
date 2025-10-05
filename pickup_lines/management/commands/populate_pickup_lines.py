from django.core.management.base import BaseCommand
from pickup_lines.models import PickupLine

class Command(BaseCommand):
    help = 'Populate the database with sample pickup lines'

    def handle(self, *args, **options):
        # Clear existing pickup lines
        PickupLine.objects.all().delete()
        
        # Romantic pickup lines
        romantic_lines = [
            "Are you a magician? Because whenever I look at you, everyone else disappears.",
            "Do you have a map? I keep getting lost in your eyes.",
            "If you were a vegetable, you'd be a cute-cumber.",
            "Are you a parking ticket? Because you've got 'fine' written all over you.",
            "Is your name Google? Because you have everything I've been searching for.",
            "Are you a camera? Because every time I look at you, I smile.",
            "Do you believe in love at first sight, or should I walk by again?",
            "Are you made of copper and tellurium? Because you're Cu-Te.",
            "If you were a fruit, you'd be a fine-apple.",
            "Are you a time traveler? Because I can see you in my future.",
            "Do you have a Band-Aid? Because I just scraped my knee falling for you.",
            "Are you a loan? Because you have my interest.",
            "Is your name Wi-Fi? Because I'm really feeling a connection.",
            "Are you a campfire? Because you're hot and I want s'more.",
            "Do you have a sunburn, or are you always this hot?"
        ]
        
        # Techy + Romantic pickup lines
        techy_lines = [
            "Are you a computer? Because you're running through my mind all the time.",
            "You must be a keyboard because you're just my type.",
            "Are you a software update? Because you make everything better.",
            "Is your name JavaScript? Because you're making my heart function properly.",
            "Are you a database? Because I can't get you out of my queries.",
            "You must be a bug in my code because you're always on my mind.",
            "Are you a compiler? Because you make my heart run without errors.",
            "Is your name Python? Because you've got me in a loop.",
            "Are you a server? Because you're always responding to my requests.",
            "You must be a variable because you're constantly on my mind.",
            "Are you a debugger? Because you help me find what's wrong with my heart.",
            "Is your name HTML? Because you're the structure of my dreams.",
            "Are you a cloud? Because you're making my heart soar.",
            "You must be a firewall because you're protecting my heart from viruses.",
            "Are you a git commit? Because you're the perfect addition to my life."
        ]
        
        # Create romantic pickup lines
        for line in romantic_lines:
            PickupLine.objects.create(text=line, category='romantic')
        
        # Create techy pickup lines
        for line in techy_lines:
            PickupLine.objects.create(text=line, category='techy')
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created {len(romantic_lines)} romantic and {len(techy_lines)} techy pickup lines!'
            )
        )
