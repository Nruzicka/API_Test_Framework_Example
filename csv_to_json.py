import req_json_segmnts


def append_gfx(csv_row: dict):
    gfx = req_json_segmnts.gfx_sgmt(
        transactionid=csv_row["TRANSACTIONID"],
        tpdtetrn=csv_row["TPDTETRN"],
        tpdteexp=csv_row["TPDTEEXP"],
        tpcntrp=csv_row["TPCNTRP"],
        tpentity=csv_row["TPENTITY"],
        notionalcur=csv_row["TPNOTIONAL"],
        notionalamt=csv_row["TPNOTIONALAMT"],
        buycur=csv_row["BUYCUR"],
        buyamt=csv_row["BUYAMT"],
        sellcur=csv_row["SELLCUR"],
        sellamt=csv_row["SELLAMT"]
        )
    return gfx


def append_product(csv_row: dict):
    product = req_json_segmnts.products_sgmt()
    match csv_row["PRODUCT"]:
        case "GFX":
            gfx_deal = append_gfx(csv_row)
            product["GUARANTEEDFXS"] = [gfx_deal]
    return product


def append_insert(csv_row: dict):
    insert = req_json_segmnts.insert_sgmt()
    match csv_row["INSERT"]:
        case "PRODUCTS":
            insert["PRODUCTS"] = append_product(csv_row)
    return insert


def append_cancel(csv_row: dict):
    cancel = req_json_segmnts.cancel_sgmt(
        transactionids = csv_row["TRANSACTIONID"]
    )
    return cancel


def append_operation(csv_row: dict):
    operation = req_json_segmnts.operation_sgmt()
    match csv_row["OPERATION"]:
        case "INSERT":
            operation["INSERT"] = append_insert(csv_row)
        case "CANCEL":
            operation["CANCEL"] = append_cancel(csv_row)
    return operation


def append_root(csv_row: dict):
    root = req_json_segmnts.root_sgmt(
        packageid=csv_row["PACKAGEID"],
        limitpreview=csv_row["LIMITPREVIEW"]
    )
    root["OPERATION"] = append_operation(csv_row)
    return root


def handle_collision(csv_row: dict, req_json: dict):
    match csv_row["PRODUCT"]:
        case "GFX":
            deal = append_gfx(csv_row)
            req_json["OPERATION"]["INSERT"]["PRODUCTS"]["GUARANTEEDFXS"].append(deal)
            


        
