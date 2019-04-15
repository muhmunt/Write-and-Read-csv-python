import csv

prasarana=[
    ('Laboratorium Multimedia','135-Ruang Praktek Siswa','12.0','8.0','Milik','Baik'),
    ('Laboratorium Komputer','301-Ruang Praktek Siswa','14.0','8.0','Milik','Baik'),
    ('Kamar Mandi/WC Guru Laki-laki','Ruang Penunjang','2.0','1.0','Milik','Baik'),
    ('Ruang Teori/Kelas','132-Ruang Teori','9.0','8.0','Milik','Baik'),
    ('Ruang Teori/Kelas','126-Ruang Teori','9.0','8.0','Milik','Baik'),
    ('Ruang TU','Ruang Penunjang','8.0','6.0','Milik','Baik'),
    ('Laboratorium Hotel','125-RPS','9.0','8.0','Milik','Baik'),
    ('Gudang','404-Ruang Penunjang','7.0','4.0','Milik','Baik'),
    ('Kamar Mandi/WC Guru Perempuan','Ruang Penunjang','2.0','1.0','Milik','Baik'),
    ('Laboratorium Komputer','302-Ruang Praktek Siswa','8.0','7.0','Milik','Baik'),
]

#target
a = open('prasarana.csv','w')
w = csv.writer(a)
w.writerow(('Jenis Prasarana','Nama','Panjang(m)','Lebar(m)','Kepemilikan','Kondisi'))

#row
for p in prasarana:
    w.writerow(p)

#close
a.close()