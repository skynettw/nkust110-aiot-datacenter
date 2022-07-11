import os, sqlite3
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()

from mysite.models import News

db = sqlite3.connect("nkustnews.db")
sql = "select * from news;"
rows = db.execute(sql)
for row in rows:
    try:
        rec = News(title=row[1],
                content=row[2],
                pdate = row[3],
                url=row[4])
        rec.save()
    except Exception as e:
        print(e)
    print(row[1])
print("All done!")