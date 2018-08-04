from bart_lib.bart import *

if __name__ == "__main__":
    # example usage
    bart = Bart()
    bart.route_info(1)
    bart.routes()
    bart.route_help()
    bart.bsa()
    bart.train_count()
    bart.elev()
    bart.elev_help()
    bart.etd('ALL')
    bart.etd('RICH', plat=2)
    bart.etd('RICH', direction='s')
    bart.etd('RICH', plat=2, direction='s')
    bart.etd_help()
    bart.version()
    bart.stninfo('24TH')
    bart.stns()
    bart.stnaccess('12th')
    bart.stn_help()
    bart.holiday()
    bart.help()
    bart.arrive("ASHB", "CIVC")
    bart.depart("ASHB", "CIVC")
    bart.fare("ASHB", "CIVC")
    bart.routesched(1)
    bart.scheds()
    bart.special()
    bart.stnsched("ASHB")