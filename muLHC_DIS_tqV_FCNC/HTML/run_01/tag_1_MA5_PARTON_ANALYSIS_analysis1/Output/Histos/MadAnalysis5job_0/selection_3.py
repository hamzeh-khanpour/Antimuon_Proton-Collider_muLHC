def selection_3():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(0.0,500.0,41,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([6.25,18.75,31.25,43.75,56.25,68.75,81.25,93.75,106.25,118.75,131.25,143.75,156.25,168.75,181.25,193.75,206.25,218.75,231.25,243.75,256.25,268.75,281.25,293.75,306.25,318.75,331.25,343.75,356.25,368.75,381.25,393.75,406.25,418.75,431.25,443.75,456.25,468.75,481.25,493.75])

    # Creating weights for histo: y4_PT_0
    y4_PT_0_weights = numpy.array([60.83877131460007,57.224351236499935,36.69948079299991,28.57747061750006,24.292000524899912,21.816060471399965,19.11335041299999,17.12797037010003,15.36473033200006,13.532070292400062,12.449130268999967,11.26438024339997,10.62110022950002,9.519652205700005,8.21920417760001,8.098878175000015,7.293618157600009,6.317124136499992,6.0487051307000135,5.7293771237999955,4.993536107899993,4.692721101400002,4.553883098399999,4.2021600907999925,4.049439087500008,3.4524360746000062,3.2904580710999967,3.2349230699,2.9665030640999985,2.730479059000008,2.4065240520000097,2.471315053400009,2.1519870464999915,2.1890110473000033,2.050173044300001,1.7956370388000042,1.6799390363000095,1.6336590352999945,1.545729033400009,1.5642400337999933])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(8.75,6.25),dpi=80)
    frame = gridspec.GridSpec(1,1)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights,\
             label="$run\_01$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, density=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"$p_{T}$ $[ t_{1} ]$ $(GeV/c)$ ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 10\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y4_PT_0_weights).max()*1.1
    #ymin=0 # linear scale
    ymin=min([x for x in (y4_PT_0_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonpositive="clip")

    # Log/Linear scale for Y-axis
    #plt.gca().set_yscale("linear")
    plt.gca().set_yscale("log",nonpositive="clip")

    # Saving the image
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_3.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_3.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_3.eps')

# Running!
if __name__ == '__main__':
    selection_3()
