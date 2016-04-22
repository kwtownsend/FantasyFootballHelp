import csv

from django.core.management.base import BaseCommand
from Players.models import Player


class Command(BaseCommand):
       # args = '<foo bar ...>'
    def _delete_table_info(self):
        print("****** Deleting all table data for fresh import ******** ")
        Player.objects.all().delete()


    def _import_from_csv(self):
        with open("nflstats/2015TOTALSTATS.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                _, created = Player.objects.get_or_create(
                    name=row[0],
                    pos=row[1],
                    fpts=row[2],
                    fptsg=row[3],
                    gp=row[4],
                    pyds=row[5],
                    ptd=row[6],
                    ryd=row[7],
                    rtd=row[8],
                    recyds=row[9],
                    rectd=row[10],
                    fum=row[11],
                    sack=row[12],
                    fr=row[13],
                    intercept=row[14],
                    td=row[15],
                    sfty=row[16],
                    fg=row[17],
                    fgmiss=row[18],
                    xpt=row[19],
                    
                )



    def handle(self, *args, **options):
        self._delete_table_info()
        self._import_from_csv()
        print("poo man shoe bitch")
