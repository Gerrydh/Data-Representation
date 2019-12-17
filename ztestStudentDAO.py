from zstudentDAO import StudentDAO

#create
latestid = StudentDAO.create(('Gerry', 41))
#find by id
result = StudentDAO.findByID(latestid);
print(result)

#update
StudentDAO.update(('Noel', 457, latestid))
result = StudentDAO.findByID(latestid);
print(result)

#get all
allStudents = StudentDAO.getAll()
for student in allStudents:
    print(student)

#delete
StudentDAO.delete(latestid)