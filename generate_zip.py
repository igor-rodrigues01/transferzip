
import subprocess
import zipfile
import shutil
import re
import os

class Upload():
    _dir         = None
    _img1        = 'adm_auto_infracao_p.shp' 
    _img2        = 'adm_embargo_a.shp'
    _destiny_dir = '/media/shp_siscom' 

    def __init__(self,dir_name='./imgs'):
        self._dir = dir_name
        self._delete_zip()
        
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)

    def _delete_zip(self):
        cur_dir = '.'
        files = os.listdir(cur_dir)
        for key in files:
            if key.endswith('.zip'):
                os.remove(key)

    def _rename_shape(self,files):
        names = []
        for key in files:
            name = re.sub(r'[^\w].+','',key)
            names.append(name)

        return names[0]

    def _delete_all(self):
        dir_name = self._dir
        files    = os.listdir(dir_name)

        if files:
            for key in files:
                os.remove(dir_name+"/"+key)

    def _create_zip(self):
        images  = os.listdir(self._dir)
        name    = self._rename_shape(images)
        zf      = zipfile.ZipFile('{}.zip'.format(name),'w')

        for key in images:
            zf.write(self._dir+"/"+key, compress_type=zipfile.ZIP_DEFLATED)

        zf.close()
        shutil.move('{}.zip'.format(name),self._destiny_dir)

    def main(self):

        self._delete_all()
        subprocess.call('ogr2ogr -f "ESRI Shapefile" '+self._dir+'/'+self._img1+' PG:"host=10.1.8.58 user=ro dbname=siscom password=ro" "ibama.adm_auto_infracao_p"',shell=True)
        self._create_zip()

        self._delete_all()
        subprocess.call('ogr2ogr -f "ESRI Shapefile" '+self._dir+'/'+self._img2+' PG:"host=10.1.8.58 user=ro dbname=siscom password=ro" "ibama.adm_embargo_a"',shell=True)
        self._create_zip()


if __name__ == '__main__':
    up = Upload()
    up.main()
