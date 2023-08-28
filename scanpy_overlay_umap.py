def feature_plot_overlay(anndata, gene1=str, gene2=str, bins = 100,title=None) : 
    umap1 = []
    umap2 = []
    
    for dot in anndata.obsm["X_umap"] :
        umap1.append(dot[0])
        umap2.append(dot[1])
    
    z1=anndata.X.T[np.where(anndata.var_names == gene1)[0][0]]
    z2=anndata.X.T[np.where(anndata.var_names == gene2)[0][0]]

        
    # Create color matrix based on the bins
    col_mat = create_square_palette(bins)
    
    # Apply binning to the values
    breaks = np.linspace(0,1,bins)
    z1_bins = np.digitize(z1, breaks) - 1
    z2_bins = np.digitize(z2, breaks) - 1
    
    colors = []
    for i in range(0,len(z1_bins)) : #binned1 and binned2 have the same length
        x = int(z1_bins[i])
        y = int(z2_bins[i])
        colors.append(col_mat[x,y])
    
    color_map_matrix = np.array(colors)

    # Create a colormap using the color map matrix
    cmap = ListedColormap(color_map_matrix)

    # Calculate the color index based on the contribution of the two variables
    #color_indices = np.round((z1 + z2) * (len(colors) - 1))

    plt.figure(figsize=(6, 6))

    # Scatter Plot
    scatter = plt.scatter(umap1, umap2, 
                          c=z1_bins + z2_bins * len(colors), 
                          cmap=cmap, s=.001 )
    plt.xlabel('UMAP1')
    plt.ylabel('UMAP2')

    if title == None :
        title=gene1 + "_" + gene2
        
    plt.title(title)

    plt.grid(False)
    # Adjust layout for both plots
    plt.tight_layout()

    # Show the plots
    plt.show()
