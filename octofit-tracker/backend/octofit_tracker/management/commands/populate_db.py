
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout
User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users (superheroes)
        users = [
            {'username': 'ironman', 'email': 'ironman@marvel.com', 'team': 'Marvel'},
            {'username': 'captainamerica', 'email': 'cap@marvel.com', 'team': 'Marvel'},
            {'username': 'batman', 'email': 'batman@dc.com', 'team': 'DC'},
            {'username': 'superman', 'email': 'superman@dc.com', 'team': 'DC'},
        ]
        for u in users:
            user = User.objects.create_user(username=u['username'], email=u['email'], password='password')
            # Optionally, add team info to user profile if extended

        # Create activities
        Activity.objects.create(user='ironman', team='Marvel', type='Running', duration=30)
        Activity.objects.create(user='batman', team='DC', type='Cycling', duration=45)
        Activity.objects.create(user='superman', team='DC', type='Swimming', duration=60)
        Activity.objects.create(user='captainamerica', team='Marvel', type='Walking', duration=20)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=50)
        Leaderboard.objects.create(team='DC', points=60)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='Easy')
        Workout.objects.create(name='Sprints', description='Run 100m sprints', difficulty='Medium')
        Workout.objects.create(name='Plank', description='Hold plank for 2 minutes', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
