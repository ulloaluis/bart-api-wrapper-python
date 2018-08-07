from bart_lib.bart import *

if __name__ == "__main__":
    # example usage
    bart = Bart()
    print(bart.bsa())
    print(bart.train_count())

    print(bart.elev())
    print(bart.elev_help())

    print(bart.etd('ALL'))

    print(bart.etd_help())

    print(bart.route_info(1))
    print(bart.routes())

    print(bart.route_help())

    print(bart.stninfo('24TH'))

    print(bart.stns())

    print(bart.stnaccess('12th'))

    print(bart.stn_help())

    print(bart.arrive("ASHB", "CIVC"))

    print(bart.depart("ASHB", "CIVC"))

    print(bart.fare("ASHB", "CIVC"))

    print(bart.routesched(1))

    print(bart.scheds())

    print(bart.special())

    print(bart.stnsched("ASHB"))

    print(bart.stn_help())

    print(bart.help())