import os 
os.environ['PROJ_LIB'] = '/anaconda3/share/proj/'  
import matplotlib #imports matplotlib
from mpl_toolkits.basemap import Basemap #imports Basemap from 'matplotlib.basemap' module
        
zoom_scale = 0.1 #sets how much to zoom in from coordinates (in degrees)

bbox = [np.min(lat)-zoom_scale,np.max(lat)+zoom_scale,
        np.min(long)-zoom_scale,np.max(long)+zoom_scale] 
#sets up the bounding box for the zoom_scale and bounds of the map

fig, ax = plt.subplots(figsize=(13,10)) #creates a subplot and sets the figure size
plt.title("Location of houses in King County") #sets the title
plt.xlabel('Longitude (degrees)', labelpad=55, fontsize=12, color='black') #sets the xlabel
plt.ylabel("Latitude (degrees)", labelpad=100, fontsize=12, color='black') #sets the ylabel

m = Basemap(projection='merc',llcrnrlat=bbox[0],urcrnrlat=bbox[1],
            llcrnrlon=bbox[2],urcrnrlon=bbox[3],lat_ts=10,resolution='i') 
#defines the projection that is going to be used, scale, the corners of the map, and the resolution

m.fillcontinents(color='dimgray') #sets the color of continents to black
m.drawparallels(np.arange(bbox[0],bbox[1],(bbox[1]-bbox[0])/5),labels=[1,0,0,0])
m.drawmeridians(np.arange(bbox[2],bbox[3],(bbox[3]-bbox[2])/5),labels=[0,0,0,1],rotation=15) 
#draw parallels, and meridians

prices_min = np.min(price) #identifies the minimal value of price
prices_max = np.max(price) #identifies the maximum value of price
cmap = plt.get_cmap('gist_rainbow') #sets the colormap
normalize = matplotlib.colors.Normalize(vmin=prices_min, vmax=prices_max)
#maps the colors in the colormap from data values stars_min to stars_vmax

#plots ranking with different colors using the numpy interpolation mapping tool
for i in range(0, len(price)): #creates a loop for values in a range
    x,y = m(long[i],lat[i]) 
    #assigns values from lists longitude and latitude to the x and y-axes
    color_interp = np.interp(price[i],[prices_min,prices_max],[0, 350]) 
    #returns the one-dimensional piecewise linear interpolant
    plt.plot(x,y,3,marker='o', color=cmap(int(color_interp))) 
    #plots houses with colors depending on their prices 

cax, fig = matplotlib.colorbar.make_axes(ax) #resizes and repositions the original axes to suit a colorbar
cbar = matplotlib.colorbar.ColorbarBase(cax, cmap=cmap,norm=normalize, label='Prices ($)') 
#draws a colorbar on existing axes 

plt.show() #shows the graph

