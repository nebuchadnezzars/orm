# SQL                                   ORM

---

table name              ⇒                               class name

field name               ⇒                                attribute name

---

English:

Any operation on the table is performed on an instance of this class using in this case Python and not SQL, the ORM software converts our python code into sql queries.

Türkçe:

**Tablodaki herhangi bir işlem(operation CRUD) bu sınıfın bir örneği(object) üzerinde gerçekleştirilir yani bu durumda SQL değil Python kullanılarak gerçekleştirilir.**

**ORM yazılımı python kodumuzu sql sorgularına dönüştürür.**

- Database’e sql sorguları ile değil ORM yazılımı ile yazıyor.
- ORM’in kendisi sql sorgularını oluşturuyor !

**ORM yapısında bir database var fakat database’de yapılan CRUD işlemleri SQL dili ile değil ORM yazılımı ile yapılıyor.** 

Python’daki ORM yazılımı: `sqlalchemy`

ORM’de SQL Injection mümkün mü?

- Eğer ORM’inde içinde prepare-statement ile parameterized kullanımının dışında, string concatenated yapıldığı bir yer var ise orada da potansiyel sql injection vardır.
- https://docs.djangoproject.com/en/5.0/releases/security/




Repodaki kodların testi için ortam hazırlayalım;


Yandaki linkten postgresql gui app’ini indir.
https://postgresapp.com/downloads.html 



postgresql’i başlat, initialized et.



Sonra aşağıdaki kodu çalıştır</br>
`sudo mkdir -p /etc/paths.d &&
echo /Applications/Postgres.app/Contents/Versions/latest/bin | sudo tee /etc/paths.d/postgresapp`</br>

`psql postgres://postgres@localhost:5432/postgres`


`ALTER USER postgres WITH PASSWORD 'postgres';`


Artık DB adı postgres olan  postgres adında parolası postgres olan 
kullanıcı var. 

`pip3 install psycopg2`<br/>


<img width="1649" alt="image" src="https://github.com/nebuchadnezzars/orm/assets/157988081/950dc3f7-807f-4add-b1a1-0b49699eb185"><br/><br/>







<img width="1582" alt="image" src="https://github.com/nebuchadnezzars/orm/assets/157988081/6f54210f-eddd-4292-acc1-ffc093eb7208"><br/><br/>





`psql postgres://postgres@localhost:5432/postgres`<br/>
`select * from student;`<br/><br/>





<img width="530" alt="image" src="https://github.com/nebuchadnezzars/orm/assets/157988081/d9fc8eda-cd76-49c5-b2e9-92813b5b0ecb"><br/>


















