# Relational & Non-Relational DB’s

`İlişkisel veri tabanı:`

- İlişkisel veritabanları, tablolar, satırlar ve sütunlardan oluşan bir yapı kullanır.
- Her tablo belirli bir türdeki verileri temsil eder ve tablolar arasında ilişkiler kurulabilir.
- MySQL, PostgreSQL, Microsoft SQL Server, Oracle. relational database’lerdir.
- ORM genellikle ilişkisel veri tabanları ile kullanılır.

`İlişkisel olmayan veri tabanı:`

- İlişkisel olmayan veritabanları, genellikle belgelere, anahtar-değer çiftlerine veya grafiklere dayalı çeşitli yapılar kullanır.
- Bu veritabanları, daha esnek ve ölçeklenebilir olabilir.
- MongoDB (Belge tabanlı), Redis (Anahtar-değer tabanlı), Neo4j (Graf tabanlı).

## ilişkisel ve ilişkisel olmayan veri tabanları farkı:

- **Veri Yapısı:** İlişkisel veritabanları, tablo, sütun ve satırlarla yapılandırılmış ilişkisel bir model kullanırken, ilişkisel olmayan veritabanları daha çeşitli yapıları destekler.
- **Esneklik:** İlişkisel veritabanları genellikle daha katı bir yapıya sahiptir ve şemaları önceden tanımlanmıştır. İlişkisel olmayan veritabanları ise daha esnek ve dinamiktir, veri modelini ihtiyaca göre değiştirmek daha kolaydır.
- İlişkisel veritabanları genellikle yapısal ve ilişkisel verilerin olduğu uygulamalarda kullanılırken, ilişkisel olmayan veritabanları genellikle büyük, dağınık veya değişken yapıdaki veri setlerini işleyen uygulamalarda tercih edilir.