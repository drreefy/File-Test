#override metode append()
    def append(self, objek):
        if not isinstance(objek, str):
            raise TypeError("objek harus bertipe string")
        self.data.append(objek)

#override metode insert
    def insert(Self, indeks, objek):
        if indeks >= len(self.data) or \
                indeks < -len(self.data):
            raise IndexError("Indeks di luar rentang")
        if not isinstance(objek, str):
            #override metode append()
            raise TypeError("Pbjek harus bertipe string")
        self.data.insert(indeks, objek)

slist = StringList()
# menambah data menggunakan metode append()
slist.append('Python')
slist.append('Ruby')
slist.append('PHP')
print(slist)

# menambah data menggunakan metode insert()
slist.insert(2, 'Perl')
print(slist)

slist.insert(-3, 'Java')
print(slist)
