import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature


def plot_satellites(latitudes, longitudes):

    ax = plt.axes(projection=ccrs.PlateCarree())

    ax.set_global()
    ax.coastlines()
    ax.add_feature(cfeature.LAND, facecolor="lightgray")
    ax.add_feature(cfeature.OCEAN)

    ax.scatter(
        longitudes,
        latitudes,
        color="red",
        s=10,
        transform=ccrs.PlateCarree()
    )

    plt.title("Satellite Positions")
    plt.show()