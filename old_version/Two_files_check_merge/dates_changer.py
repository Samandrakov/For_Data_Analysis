from datetime import datetime

import pandas as pd
import pandas as ps

df = pd.read_excel('dates.xlsx')

dates = df.iloc[:,0].tolist()
print(dates)
# Пример списка дат
# dates = ["1839.01.01", "1840.02.15", "1841.03.20"]




# Функция для преобразования формата даты
def convert_date(date_str):
    date_obj = datetime.strptime(date_str, "%Y.%m.%d")
    return date_obj.strftime("%d.%m.%Y")

# Преобразование всех дат в списке
converted_dates = [convert_date(date) for date in dates]

for i in range(len(converted_dates)):
    print(converted_dates[i])
# print(converted_dates)

C:\Users\Данила\AppData\Local\Programs\Python\Python311\python.exe C:\Users\Данила\Desktop\pythonProject\For_Data_Analysis\Two_files_check_merge\dates_changer.py
['1839.01.01', '1882.08.05', '1837.10.31', '1886.01.01', '1784.01.01', '1879.01.01', '1886.01.01', '1866.01.01', '1837.01.01', '1896.10.01', '1852.01.01', '1892.01.01', '1888.01.01', '1850.01.01', '1865.01.01', '1849.01.01', '1864.01.01', '1847.10.01', '1869.01.01', '1809.08.16', '1836.01.01', '1885.01.01', '1875.01.01', '1812.06.16', '1890.02.05', '1873.01.01', '1837.01.01', '1855.01.01', '1854.01.01', '1806.06.02', '1873.01.01', '1806.01.01', '1848.01.01', '1879.01.01', '1872.01.01', '1833.01.01', '1881.01.01', '1866.01.01', '1871.01.01', '1893.06.23', '1755.01.09', '1668.01.01', '1899.04.07', '1897.01.01', '1889.09.23', '1845.01.01', '1698.01.01', '1817.06.23', '1850.01.01', '1800.01.01', '1835.01.01', '1832.03.30', '1864.07.12', '1872.01.01', '1868.01.01', '1876.01.01', '1894.01.01', '1887.01.01', '1853.01.01', '1872.01.01', '1885.01.01', '1895.12.16', '1895.01.01', '1865.04.06', '1894.01.01', '1875.01.01', '1665.01.01', '1831.01.01', '1836.01.01', '1853.01.01', '1890.01.01', '1880.01.01', '1894.01.01', '1859.01.01', '1882.01.01', '1886.08.08', '1879.01.01', '1866.01.01', '1727.01.01', '1863.01.01', '1876.09.26', '1870.03.10', '1802.07.19', '1796.01.01', '1823.01.01', '1809.01.01', '1899.01.01', '1810.01.01', '1883.01.01', '1881.01.01', '1865.01.01', '1868.03.23', '1886.01.01', '1847.01.01', '1889.05.28', '1868.10.22', '1874.01.01', '1898.04.25', '1846.01.01', '1848.05.30', '1897.03.08', '1832.07.01', '1871.10.05', '1858.06.17', '1856.01.01', '1896.01.01', '1891.05.15', '1889.01.01', '1853.01.01', '1899.01.01', '1899.07.17', '1899.01.01', '1853.01.01', '1792.01.01', '1865.05.12', '1876.01.01', '1857.01.01', '1874.01.01', '1864.01.01', '1870.01.01', '1882.01.01', '1871.01.01', '1882.01.01', '1874.01.01', '1862.01.01', '1866.01.01', '1669.01.01', '1870.01.01', '1880.01.01', '1883.01.01', '1758.01.01', '1884.01.01', '1889.01.01', '1886.01.01', '1546.01.01', '1822.01.01', '1889.01.01', '1847.01.01', '1890.01.01', '1897.01.01', '1891.01.01', '1828.01.01', '1862.01.01', '1887.01.01', '1894.05.19', '1886.01.01', '1898.12.24', '1892.01.01', '1881.01.01', '1898.01.01', '1814.01.01', '1885.01.01', '1888.01.01', '1860.01.01', '1869.01.01', '1859.01.01', '1847.01.01', '1878.01.01', '1792.01.01', '1884.01.01', '1828.01.01', '1897.01.01', '1805.01.01', '1889.01.01', '1893.10.01', '1826.01.01', '1897.01.01', '1834.04.12', '1860.01.01', '1872.09.17', '1826.01.01', '1856.01.01', '1288.01.01', '1899.02.01', '1783.01.01', '1774.01.01', '1895.01.01', '1885.01.01', '1899.01.01', '1851.08.01', '1890.08.23', '1889.01.01', '1834.01.01', '1872.01.01', '1885.01.01', '1874.01.01', '1783.01.01', '1888.01.01', '1788.01.26', '1886.01.01', '1850.01.01', '1898.01.01', '1845.01.01', '1590.01.01', '1892.01.01', '1873.01.01', '1897.04.15', '1837.06.19', '1851.09.18', '1895.10.01', '1890.01.01', '1864.01.01', '1855.01.01', '1898.01.01', '1876.01.01', '1888.01.01', '1863.01.01', '1875.01.24', '1898.01.01', '1804.01.01', '1867.01.01', '1841.01.01', '1888.01.01', '1869.01.01', '1886.01.01', '1846.01.01', '1853.01.01', '1890.01.01', '1853.01.01', '1887.01.01', '1881.01.01', '1880.01.01', '1858.01.01', '1865.01.01', '1889.01.01', '1878.01.01', '1839.01.01', '1857.01.01', '1742.01.01', '1472.03.13', '1849.01.01', '1888.01.01', '1873.01.01', '1890.01.01', '1868.01.01', '1893.01.01', '1235.01.01', '1872.01.28', '1852.01.01', '1862.01.01', '1857.01.01', '1866.01.01', '1888.01.01', '1874.01.01', '1881.01.01', '1888.01.01', '1889.01.01', '1802.06.03', '1850.01.01', '1899.01.01', '1866.09.06', '1834.01.01', '1554.01.01', '1853.12.05', '1650.01.01', '1889.06.01', '1889.01.01', '1853.01.01', '1899.01.01', '1899.01.01', '1834.01.01', '1887.01.01', '1882.01.01', '1858.10.28', '1860.01.01', '1864.02.04', '1899.01.01', '1891.01.01', '1882.01.01', '1898.01.01', '1845.01.01', '1852.01.01', '1873.01.01', '1899.01.01', '1767.01.01', '1859.01.01', '1886.01.01', '1888.01.01', '1858.07.09', '1824.01.01', '1851.04.08', '1887.01.01', '1804.01.01', '1807.01.01', '1837.09.12', '1899.01.01', '1869.06.01', '1856.01.01', '1817.01.01', '1845.01.01', '1890.01.01', '1864.01.01', '1889.01.01', '1819.01.01', '1866.01.01', '1783.01.01', '1850.01.01', '1859.01.01', '1848.07.12', '1534.01.01', '1895.01.01', '1897.11.01', '1891.01.01', '1871.01.01', '1891.01.01', '1890.01.01', '1876.01.01', '1880.05.18', '1880.01.01', '1894.01.01', '1882.01.01', '1889.01.01', '1861.01.01', '1864.01.01', '1792.01.01', '1882.01.01', '1845.01.01', '1883.01.01', '1882.01.01', '1885.01.01', '1886.10.14', '1878.01.01', '1882.01.01', '1811.01.01', '1892.01.01', '1889.01.01', '1876.03.11', '1858.01.01', '1895.01.01', '1886.01.01', '1872.01.01', '1896.01.01', '1871.01.01', '1889.10.03', '1834.01.01', '1859.01.01', '1887.01.28', '1880.01.01', '1897.12.17', '1865.01.01', '1832.01.01', '1896.01.01', '1896.01.01', '1877.01.01', '1863.01.01', '1782.01.01', '1849.01.01', '1867.01.01', '1855.01.01', '1891.01.01', '1878.01.01', '1870.01.01', '1884.01.01', '1737.01.01', '1893.01.01', '1888.01.01', '1890.01.01', '1866.12.11', '1890.01.01', '1898.01.01', '1755.01.01', '1870.01.20', '1785.01.01', '1892.01.01', '1896.01.01', '1859.01.01', '1896.01.01', '1649.01.01', '1877.01.01', '1859.01.01', '1189.05.14', '1870.01.01', '1863.01.01', '1866.01.01', '1851.01.01', '1886.01.01', '1875.01.01', '1600.01.01', '1894.01.01', '1884.01.01', '1868.01.01', '1886.01.01', '1883.01.01', '1897.05.14', '1890.01.01', '1897.11.01', '1875.01.01', '1889.01.01', '1897.01.01', '1891.10.13', '1884.03.28', '1888.01.01', '1883.01.01', '1878.01.01', '1846.01.01', '1869.04.12', '1896.01.01', '1864.03.31', '1895.01.01', '1838.01.01', '1825.01.01', '1893.01.01', '1819.01.01', '1878.01.01', '1836.01.01', '1855.01.01', '1899.01.01', '1830.01.01', '1869.01.01', '1862.01.01', '1858.01.01', '1881.01.01', '1805.01.01', '1800.01.01', '1872.01.01', '1887.01.01', '1875.01.01', '1880.01.01', '1896.01.01', '1887.12.27', '1885.01.01', '1896.01.01', '1879.01.01', '1879.01.01', '1893.01.01', '1896.03.24', '1895.01.01', '1894.05.03', '1863.01.01', '1892.01.01', '1888.01.01', '1872.01.01', '1886.01.01', '1878.11.02', '1887.01.01', '1838.01.01', '1853.01.01', '1892.12.09', '1864.01.01', '1850.01.01', '1873.01.01', '1858.01.01', '1854.02.15', '1895.01.01', '1867.01.01', '1321.01.01', '1890.01.01', '1886.01.01', '1893.09.28', '1890.01.01', '1883.01.01', '1200.01.01', '1851.01.01', '1885.01.01', '1821.01.01', '1871.01.01', '1630.01.01']
01.01.1839
05.08.1882
31.10.1837
01.01.1886
01.01.1784
01.01.1879
01.01.1886
01.01.1866
01.01.1837
01.10.1896
01.01.1852
01.01.1892
01.01.1888
01.01.1850
01.01.1865
01.01.1849
01.01.1864
01.10.1847
01.01.1869
16.08.1809
01.01.1836
01.01.1885
01.01.1875
16.06.1812
05.02.1890
01.01.1873
01.01.1837
01.01.1855
01.01.1854
02.06.1806
01.01.1873
01.01.1806
01.01.1848
01.01.1879
01.01.1872
01.01.1833
01.01.1881
01.01.1866
01.01.1871
23.06.1893
09.01.1755
01.01.1668
07.04.1899
01.01.1897
23.09.1889
01.01.1845
01.01.1698
23.06.1817
01.01.1850
01.01.1800
01.01.1835
30.03.1832
12.07.1864
01.01.1872
01.01.1868
01.01.1876
01.01.1894
01.01.1887
01.01.1853
01.01.1872
01.01.1885
16.12.1895
01.01.1895
06.04.1865
01.01.1894
01.01.1875
01.01.1665
01.01.1831
01.01.1836
01.01.1853
01.01.1890
01.01.1880
01.01.1894
01.01.1859
01.01.1882
08.08.1886
01.01.1879
01.01.1866
01.01.1727
01.01.1863
26.09.1876
10.03.1870
19.07.1802
01.01.1796
01.01.1823
01.01.1809
01.01.1899
01.01.1810
01.01.1883
01.01.1881
01.01.1865
23.03.1868
01.01.1886
01.01.1847
28.05.1889
22.10.1868
01.01.1874
25.04.1898
01.01.1846
30.05.1848
08.03.1897
01.07.1832
05.10.1871
17.06.1858
01.01.1856
01.01.1896
15.05.1891
01.01.1889
01.01.1853
01.01.1899
17.07.1899
01.01.1899
01.01.1853
01.01.1792
12.05.1865
01.01.1876
01.01.1857
01.01.1874
01.01.1864
01.01.1870
01.01.1882
01.01.1871
01.01.1882
01.01.1874
01.01.1862
01.01.1866
01.01.1669
01.01.1870
01.01.1880
01.01.1883
01.01.1758
01.01.1884
01.01.1889
01.01.1886
01.01.1546
01.01.1822
01.01.1889
01.01.1847
01.01.1890
01.01.1897
01.01.1891
01.01.1828
01.01.1862
01.01.1887
19.05.1894
01.01.1886
24.12.1898
01.01.1892
01.01.1881
01.01.1898
01.01.1814
01.01.1885
01.01.1888
01.01.1860
01.01.1869
01.01.1859
01.01.1847
01.01.1878
01.01.1792
01.01.1884
01.01.1828
01.01.1897
01.01.1805
01.01.1889
01.10.1893
01.01.1826
01.01.1897
12.04.1834
01.01.1860
17.09.1872
01.01.1826
01.01.1856
01.01.1288
01.02.1899
01.01.1783
01.01.1774
01.01.1895
01.01.1885
01.01.1899
01.08.1851
23.08.1890
01.01.1889
01.01.1834
01.01.1872
01.01.1885
01.01.1874
01.01.1783
01.01.1888
26.01.1788
01.01.1886
01.01.1850
01.01.1898
01.01.1845
01.01.1590
01.01.1892
01.01.1873
15.04.1897
19.06.1837
18.09.1851
01.10.1895
01.01.1890
01.01.1864
01.01.1855
01.01.1898
01.01.1876
01.01.1888
01.01.1863
24.01.1875
01.01.1898
01.01.1804
01.01.1867
01.01.1841
01.01.1888
01.01.1869
01.01.1886
01.01.1846
01.01.1853
01.01.1890
01.01.1853
01.01.1887
01.01.1881
01.01.1880
01.01.1858
01.01.1865
01.01.1889
01.01.1878
01.01.1839
01.01.1857
01.01.1742
13.03.1472
01.01.1849
01.01.1888
01.01.1873
01.01.1890
01.01.1868
01.01.1893
01.01.1235
28.01.1872
01.01.1852
01.01.1862
01.01.1857
01.01.1866
01.01.1888
01.01.1874
01.01.1881
01.01.1888
01.01.1889
03.06.1802
01.01.1850
01.01.1899
06.09.1866
01.01.1834
01.01.1554
05.12.1853
01.01.1650
01.06.1889
01.01.1889
01.01.1853
01.01.1899
01.01.1899
01.01.1834
01.01.1887
01.01.1882
28.10.1858
01.01.1860
04.02.1864
01.01.1899
01.01.1891
01.01.1882
01.01.1898
01.01.1845
01.01.1852
01.01.1873
01.01.1899
01.01.1767
01.01.1859
01.01.1886
01.01.1888
09.07.1858
01.01.1824
08.04.1851
01.01.1887
01.01.1804
01.01.1807
12.09.1837
01.01.1899
01.06.1869
01.01.1856
01.01.1817
01.01.1845
01.01.1890
01.01.1864
01.01.1889
01.01.1819
01.01.1866
01.01.1783
01.01.1850
01.01.1859
12.07.1848
01.01.1534
01.01.1895
01.11.1897
01.01.1891
01.01.1871
01.01.1891
01.01.1890
01.01.1876
18.05.1880
01.01.1880
01.01.1894
01.01.1882
01.01.1889
01.01.1861
01.01.1864
01.01.1792
01.01.1882
01.01.1845
01.01.1883
01.01.1882
01.01.1885
14.10.1886
01.01.1878
01.01.1882
01.01.1811
01.01.1892
01.01.1889
11.03.1876
01.01.1858
01.01.1895
01.01.1886
01.01.1872
01.01.1896
01.01.1871
03.10.1889
01.01.1834
01.01.1859
28.01.1887
01.01.1880
17.12.1897
01.01.1865
01.01.1832
01.01.1896
01.01.1896
01.01.1877
01.01.1863
01.01.1782
01.01.1849
01.01.1867
01.01.1855
01.01.1891
01.01.1878
01.01.1870
01.01.1884
01.01.1737
01.01.1893
01.01.1888
01.01.1890
11.12.1866
01.01.1890
01.01.1898
01.01.1755
20.01.1870
01.01.1785
01.01.1892
01.01.1896
01.01.1859
01.01.1896
01.01.1649
01.01.1877
01.01.1859
14.05.1189
01.01.1870
01.01.1863
01.01.1866
01.01.1851
01.01.1886
01.01.1875
01.01.1600
01.01.1894
01.01.1884
01.01.1868
01.01.1886
01.01.1883
14.05.1897
01.01.1890
01.11.1897
01.01.1875
01.01.1889
01.01.1897
13.10.1891
28.03.1884
01.01.1888
01.01.1883
01.01.1878
01.01.1846
12.04.1869
01.01.1896
31.03.1864
01.01.1895
01.01.1838
01.01.1825
01.01.1893
01.01.1819
01.01.1878
01.01.1836
01.01.1855
01.01.1899
01.01.1830
01.01.1869
01.01.1862
01.01.1858
01.01.1881
01.01.1805
01.01.1800
01.01.1872
01.01.1887
01.01.1875
01.01.1880
01.01.1896
27.12.1887
01.01.1885
01.01.1896
01.01.1879
01.01.1879
01.01.1893
24.03.1896
01.01.1895
03.05.1894
01.01.1863
01.01.1892
01.01.1888
01.01.1872
01.01.1886
02.11.1878
01.01.1887
01.01.1838
01.01.1853
09.12.1892
01.01.1864
01.01.1850
01.01.1873
01.01.1858
15.02.1854
01.01.1895
01.01.1867
01.01.1321
01.01.1890
01.01.1886
28.09.1893
01.01.1890
01.01.1883
01.01.1200
01.01.1851
01.01.1885
01.01.1821
01.01.1871
01.01.1630

Process finished with exit code 0


