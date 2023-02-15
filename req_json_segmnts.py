
def flows_sgmt(
famout,
famtfxd,
fccnom,
fccnomu,
fcurfxd,
fcurrency,
ftype,
ftypelab0,
ftypelab1,
ftypelab2,
ftypelab4,
fvalue,
hfstlmtd
):
    flows = {
        "FAMOUNT": famout,
        "FAMTFXD": famtfxd,
        "FCCNOM": fccnom,
        "FCCNOMU": fccnomu,
        "FCURFXD": fcurfxd,
        "FCURRENCY": fcurrency,
        "FTYPE": ftype,
        "FTYPELAB0": ftypelab0,
        "FTYPELAB1": ftypelab1,
        "FTYPELAB2": ftypelab2,
        "FTYPELAB4": ftypelab4,
        "FVALUE": fvalue,
        "HFSTLMTD": hfstlmtd,
     }
    return flows


def fxswaps_sgmt(
    flows: list = None,
    tpexrate=0,
    tpexrate2=0,
    tpnominal=0,
    tpnominal2=0,
    tpdteexp="",
    tpdteexp2="",
    tpfxund="",
    tpnomcur="",
    tpbuy="",
    tpprod="",
    trnfmly="",
    trngrp="",
    trntype="",
    tpfxbase="",
    tpcntrp="",
    tpentity="",
    tpiqty=0,
    tpqtyeq=0,
    tpdvcs="",
    country="",
    tptrader="",
    tpdtetrn="",
    tpsptfwd="",
    tpbrolbl="",
    transactionid=""
):
    fxswaps = {
        "FLOWS": flows,
        "TPEXRATE": tpexrate,
        "TPEXRATE2": tpexrate2,
        "TPNOMINAL": tpnominal,
        "TPNOMINAL2": tpnominal2,
        "TPDTEEXP": tpdteexp,
        "TPDTEEXP2": tpdteexp2,
        "TPFXUND": tpfxund,
        "TPNOMCUR": tpnomcur,
        "TPBUY": tpbuy,
        "TPPROD": tpprod,
        "TRNFMLY": trnfmly,
        "TRNGRP": trngrp,
        "TRNTYPE": trntype,
        "TPFXBASE": tpfxbase,
        "TPCNTRP": tpcntrp,
        "TPENTITY": tpentity,
        "TPIQTY": tpiqty,
        "TPQTYEQ": tpqtyeq,
        "TPDVCS": tpdvcs,
        "COUNTRY": country,
        "TPTRADER": tptrader,
        "TPDTETRN": tpdtetrn,
        "TPSPTFWD": tpsptfwd,
        "TPBROLBL": tpbrolbl,
        "TRANSACTIONID": transactionid
    }    
    return fxswaps


def fxsptfwd_sgmt(
    flows: list = None,
    tpexrate=0,
    tpnominal=0,
    tpdteexp="",
    tpfxund="",
    tpnomcur="",
    tpbuy="",
    tpprod="",
    trnfmly="",
    trngrp="",
    trntype="",
    tpfxbase="",
    tpcntrp="",
    tpentity="",
    tpiqty=0,
    tpqtyeq=0,
    tpdvcs="",
    country="",
    tptrader="",
    tpdtetrn="",
    tpsptfwd="",
    tpbrolbl="",
    transactionid=""
):
    fxspotforwards = {
        "FLOWS": flows,
        "TPEXRATE": tpexrate,
        "TPNOMINAL": tpnominal,
        "TPDTEEXP": tpdteexp,
        "TPFXUND": tpfxund,
        "TPNOMCUR": tpnomcur,
        "TPBUY": tpbuy,
        "TPPROD": tpprod,
        "TRNFMLY": trnfmly,
        "TRNGRP": trngrp,
        "TRNTYPE": trntype,
        "TPFXBASE": tpfxbase,
        "TPCNTRP": tpcntrp,
        "TPENTITY": tpentity,
        "TPIQTY": tpiqty,
        "TPQTYEQ": tpqtyeq,
        "TPDVCS": tpdvcs,
        "COUNTRY": country,
        "TPTRADER": tptrader,
        "TPDTETRN": tpdtetrn,
        "TPSPTFWD": tpsptfwd,
        "TPBROLBL": tpbrolbl,
        "TRANSACTIONID": transactionid
    }
    return fxspotforwards


def gfx_sgmt(
    transactionid="",
    tpdtetrn="",
    tpdteexp="",
    tpcntrp="",
    tpentity="",
    notionalcur="",
    notionalamt=0,
    buycur="",
    buyamt=0,
    sellcur="",
    sellamt=0
):
    gfx = {
        "TRANSACTIONID": transactionid,
        "TPDTETRN": tpdtetrn,
        "TPDTEEXP": tpdteexp,
        "TPCNTRP": tpcntrp,
        "TPENTITY": tpentity,
        "NOTIONALCUR": notionalcur,
        "NOTIONALAMT": notionalamt,
        "BUYCUR": buycur,
        "BUYAMT": buyamt,
        "SELLCUR": sellcur,
        "SELLAMT": sellamt 
    }
    return gfx


def products_sgmt(
    fxswaps: list = None,
    fxspotforwards: list = None,
    irs: list = None,
    structureadhocs: list = None,
    trax: list = None,
    gfx: list = None
):
    products = {
        "FXSWAPS": fxswaps,
        "FXSPOTFORWARDS": fxspotforwards,
        "IRS": irs,
        "STRUCTUREADHOCS": structureadhocs,
        "TRAX": trax,
        "GUARANTEEDFXS": gfx
    }
    return products


def insert_sgmt(products=None):
    insert = {
        "PRODUCTS": products
    }
    return insert


def cancel_sgmt(transactionids: list = None):
    cancel = {
        "TRANSACTIONIDS": transactionids
    }
    return cancel


def operation_sgmt(
    insert=None,
    cancel=None,
    modify=None,
    acknowledge=None
):
    operation = {
        "INSERT": insert,
        "CANCEL": cancel,
        "MODIFY": modify,
        "ACKNOWLEDGE": acknowledge
    }
    return operation


def override_sgmt(
    remarks="",
    overrides: list = None
):
    override = {
        "REMARKS": remarks,
        "OVERRIDES": overrides
    }
    return override


def root_sgmt(
    packageid="",
    timestamp="",
    sourcesystem="",
    limitpreview=0,
    operation=None,
    controllerid="",
    version="",
    sourcetraceid="",
    override=None
):
    root = {
        "PACKAGEID": packageid,
        "TIMESTAMP": timestamp,
        "SOURCESYSTEM": sourcesystem,
        "LIMITPREVIEW": limitpreview,
        "OPERATION": operation,
        "CONTROLLERID": controllerid,
        "VERSION": version,
        "SOURCETRACEID": sourcetraceid,
        "OVERRIDE": override
    }
    return root