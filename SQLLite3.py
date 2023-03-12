#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sqlite3                # tạo connection (kết nối) - ở đây là mở file example.db
conn = sqlite3.connect('sql-murder-mystery.db')
# tạo cursor
c = conn.cursor()

# Save (commit) thay đổi

for row in c.execute("""SELECT person.name, interview.transcript
                        FROM person JOIN interview
                        ON person.id = interview.person_id
                        WHERE person.id = 14887 OR person.id = 16371""").fetchall():
    print(row)
# Luôn đóng connection sau khi đã xong việc
conn.close()


# ### Clue:
# 'Get Fit Now Gym'
# Membership number: "48Z%"
# lastweek / Jan 9th
# 

# In[8]:


conn = sqlite3.connect('sql-murder-mystery.db')
c = conn.cursor()
for row in c.execute("""SELECT membership_id, check_in_date
                        FROM get_fit_now_check_in
                        WHERE membership_id LIKE '48Z%'""").fetchall():
    print(row)
# Luôn đóng connection sau khi đã xong việc
conn.close()


# In[15]:


conn = sqlite3.connect('sql-murder-mystery.db')
c = conn.cursor()
for row in c.execute("""SELECT id, person_id, membership_status
                        FROM get_fit_now_member
                        WHERE id = '48Z7A' OR id = '48Z55'
                        """).fetchall():
    print(row)
# Luôn đóng connection sau khi đã xong việc
conn.close()


# In[19]:


conn = sqlite3.connect('sql-murder-mystery.db')
c = conn.cursor()
for row in c.execute("""SELECT name,person.id, license_id, plate_number
                        FROM drivers_license
                        JOIN person
                          ON person.license_id = drivers_license.id
                        WHERE person.id = 28819 OR person.id = 67318
                        """).fetchall():
    print(row)
# Luôn đóng connection sau khi đã xong việc
conn.close()


# In[25]:


conn = sqlite3.connect('sql-murder-mystery.db')
c = conn.cursor()
for k, v in c.execute("""SELECT person.name, interview.transcript
                        FROM person JOIN interview
                        ON person.id = interview.person_id
                        WHERE person.id = 67318
                        """).fetchall():
    print(k, v)
# Luôn đóng connection sau khi đã xong việc
conn.close()


# In[83]:


print('-'*100)

query = """
SELECT name, p.id, gender, car_model as car, hair_color as hair, height, event_name
FROM drivers_license dl
JOIN person p
ON p.license_id = dl.id
JOIN facebook_event_checkin fb
ON p.id = fb.person_id
WHERE car=? AND gender=? AND hair=? AND event_name =?
LIMIT 1
"""
conn = sqlite3.connect('sql-murder-mystery.db')
c = conn.cursor()
t = ('Model S','female', 'red', 'SQL Symphony Concert')
for row in c.execute(query, t).fetchall():
    print(row)
# Luôn đóng connection sau khi đã xong việc
conn.close()

print('-'*100)

# In[ ]:




