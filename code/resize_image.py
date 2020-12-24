from PIL import Image
import numpy as np
 
output_path_graph= '/Users/davidan/Desktop/Github/cogs9_\
spotify_study/visualization/'
billboard = 'spotify_billboard_merged_%s.png'
billboard_range = np.arange(1958, 1960)

for r in billboard_range:
    img = Image.open(output_path_graph+billboard%(str(r)))

    print('Original Dimensions : ',img.size)
    
    # resize image
    resized = img.resize((201, 133), Image.ANTIALIAS)
    
    print('Resized Dimensions : ',resized.size)
    
    resized.save(output_path_graph+billboard%(str(r)+'_ds'), quality=95, subsampling=0)
