def selection_5():

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

    # Creating weights for histo: y6_PT_0
    y6_PT_0_weights = numpy.array([0.002869761090176277,0.0018522010582015678,0.0008569159269268017,0.0004960099155860805,0.00031149360978803916,0.0002039619064090789,0.00014627790459647907,0.0001011465031783186,7.966923250344002e-05,5.6523071776120035e-05,4.868675152987996e-05,3.722251116964003e-05,3.018434094848017e-05,2.5685710807120068e-05,1.9228000604199948e-05,1.6543340519840085e-05,1.3495880424079987e-05,1.1827040371640159e-05,8.997254282720013e-06,9.360046294119998e-06,7.763759243959996e-06,6.67538220976001e-06,5.514446173280008e-06,4.353510136800007e-06,4.4986271413600065e-06,2.757223086640004e-06,3.7004831162799894e-06,1.3786110433199863e-06,1.6688450524399868e-06,2.684664084359988e-06,1.3786110433199863e-06,1.1609360364800015e-06,1.5237280478799865e-06,1.1609360364800015e-06,1.5237280478799865e-06,6.530265205200009e-07,1.3060530410400019e-06,7.255850228000011e-07,7.981435250800012e-07,8.707020273600012e-07])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(8.75,6.25),dpi=80)
    frame = gridspec.GridSpec(1,1)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y6_PT_0_weights,\
             label="$run\_02$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, density=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"$p_{T}$ $[ mu+_{1} ]$ $(GeV/c)$ ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 10\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y6_PT_0_weights).max()*1.1
    #ymin=0 # linear scale
    ymin=min([x for x in (y6_PT_0_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonpositive="clip")

    # Log/Linear scale for Y-axis
    #plt.gca().set_yscale("linear")
    plt.gca().set_yscale("log",nonpositive="clip")

    # Saving the image
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_5.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_5.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_5.eps')

# Running!
if __name__ == '__main__':
    selection_5()
