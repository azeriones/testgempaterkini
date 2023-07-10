import deteksigempa

if __name__ == '__main__':
    print('Aplikasi Utama')
    result = deteksigempa.ekstraksi_data()
    deteksigempa.tampilkan_data(result)
