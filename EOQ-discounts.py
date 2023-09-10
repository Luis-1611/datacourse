from typing import List

import pandas as pd

#Demand of ingredients
#The demand of every ingredient comes from their proportion in the chocolate bars.
#At the same time, the demand of chocolate bars is calculated from the cartons annual forecast.
cartons= 14671
#Each carton contains 100 bags with 20 chocolate bars per bag.
num_bar= cartons*100*20
print("The total number of bars to be produced in 2011 is:",num_bar,"\n")

ingredients= ["Cocoa Powder","Cocoa Butter","Dark Chocolate","Dry fruits and Nuts"]
ingr_prop= [5.1,6.2,7.8,4]

kg=[]
for i in ingr_prop:
     ing_demand= float(i*num_bar/1000)
     kg.append(ing_demand)

print("Demand in kg of the ingredients and related costs:")
data = {"Ingredients": ingredients,
         "Demand (kg)": kg,
        "Ordering cost":[1000,1200,800,2100],
        "Carrying cost":[0.4,0.30,0.35,0.25]}
df = pd.DataFrame(data)
print(df,"\n")

#Quantity of each ingredient to be ordered
#COCOA POWDER
unit_cost_cp=[120.3,120.2,120.1,120]
l_limit1=[1,2001,4001,6001]
u_limit1=[2000,4000,6000,1000000000]
ranges1={"Lower":l_limit1,
        "Upper":u_limit1}
ranges_cp_df=pd.DataFrame(ranges1)
print(ranges_cp_df)
eoq_cp=[]
boq_cp=[]
trc_cp=[]

#COCOA BUTTER
unit_cost_cb=[240.2,240.15,240.10,240.05]
l_limit2=[1,1001,2001,3001]
u_limit2=[1000,2000,3000,1000000000]
ranges2={"Lower":l_limit2,
        "Upper":u_limit2}
ranges_cb_df=pd.DataFrame(ranges2)
#print(ranges_cb_df)
eoq_cb=[]
boq_cb=[]
trc_cb=[]

#DARK CHOCOLATE
unit_cost_dc=[300.90,300.80,300.70,300.60]
l_limit3=[1,1251,2501,3571]
u_limit3=[1250,2500,3570,1000000000]
ranges3={"Lower":l_limit3,
        "Upper":u_limit3}
ranges_dc_df=pd.DataFrame(ranges3)
#print(ranges_dc_df)
eoq_dc=[]
boq_dc=[]
trc_dc=[]

#DRY FRUITS AND NUTS
unit_cost_dfn=[361,360.80,360.60,360.40]
l_limit4=[1,2501,5001,7501]
u_limit4=[2500,5000,7500,1000000000]
ranges4={"Lower":l_limit4,
        "Upper":u_limit4}
ranges_dfn_df=pd.DataFrame(ranges4)
#print(ranges_dfn_df)
eoq_dfn=[]
boq_dfn=[]
trc_dfn=[]

for i in range(0,4):
    for j in range(0,4):
        if i==0:
            eoq= round((2*df.at[i,"Ordering cost"]*df.at[i,"Demand (kg)"])/(unit_cost_cp[j]*df.at[i,"Carrying cost"]))**(1/2)
            if ranges_cp_df.at[j,"Lower"]<=eoq<=ranges_cp_df.at[j,"Upper"]:
                trc= round((df.at[i,"Ordering cost"])*(df.at[i,"Demand (kg)"]/eoq)+(eoq/2)*(unit_cost_cp[j])*(df.at[i,"Carrying cost"])+(df.at[i,"Demand (kg)"])*(unit_cost_cp[j]))
                eoq_cp.append(eoq)
                boq_cp.append(eoq)
                trc_cp.append(trc)
            else:
                if abs(eoq-ranges_cp_df.at[j,"Lower"])<abs(eoq-ranges_cp_df.at[j,"Upper"]):
                    q= ranges_cp_df.at[j,"Lower"]
                    eoq_cp.append(eoq)
                    boq_cp.append(q)
                    trc=round((df.at[i,"Ordering cost"])*(df.at[i,"Demand (kg)"]/q)+(q/2)*(unit_cost_cp[j])*(df.at[i,"Carrying cost"])+(df.at[i,"Demand (kg)"])*(unit_cost_cp[j]))
                    trc_cp.append(trc)
                else:
                    q = ranges_cp_df.at[j, "Upper"]
                    eoq_cp.append(eoq)
                    boq_cp.append(q)
                    trc = round((df.at[i, "Ordering cost"]) * (df.at[i, "Demand (kg)"] / q) + (q / 2) * (unit_cost_cp[j])*(df.at[i, "Carrying cost"]) + (df.at[i, "Demand (kg)"]) * (unit_cost_cp[j]))
                    trc_cp.append(trc)

        if i==1:
            eoq = round((2 * df.at[i, "Ordering cost"] * df.at[i, "Demand (kg)"]) / (unit_cost_cb[j] * df.at[i, "Carrying cost"])) ** (1 / 2)
            if ranges_cb_df.at[j, "Lower"] <= eoq <= ranges_cb_df.at[j, "Upper"]:
                trc = round((df.at[i, "Ordering cost"]) * (df.at[i, "Demand (kg)"] / eoq) + (eoq / 2) * (unit_cost_cb[j]) * (df.at[i, "Carrying cost"]) + (df.at[i, "Demand (kg)"]) * (unit_cost_cb[j]))
                eoq_cb.append(eoq)
                boq_cb.append(eoq)
                trc_cb.append(trc)
            else:
                if abs(eoq - ranges_cb_df.at[j, "Lower"]) < abs(eoq - ranges_cb_df.at[j, "Upper"]):
                    q = ranges_cb_df.at[j, "Lower"]
                    eoq_cb.append(eoq)
                    boq_cb.append(q)
                    trc = round((df.at[i, "Ordering cost"]) * (df.at[i, "Demand (kg)"] / q) + (q / 2) * (unit_cost_cb[j]) * (df.at[i, "Carrying cost"]) + (df.at[i, "Demand (kg)"]) * (unit_cost_cb[j]))
                    trc_cb.append(trc)
                else:
                    q = ranges_cb_df.at[j, "Upper"]
                    eoq_cb.append(eoq)
                    boq_cb.append(q)
                    trc = round((df.at[i, "Ordering cost"]) * (df.at[i, "Demand (kg)"] / q) + (q / 2) * (unit_cost_cb[j]) * (df.at[i, "Carrying cost"]) + (df.at[i, "Demand (kg)"]) * (unit_cost_cb[j]))
                    trc_cb.append(trc)
        if i==2:
            eoq = round((2 * df.at[i, "Ordering cost"] * df.at[i, "Demand (kg)"]) / (unit_cost_dc[j] * df.at[i, "Carrying cost"])) ** (1 / 2)
            if ranges_dc_df.at[j, "Lower"] <= eoq <= ranges_dc_df.at[j, "Upper"]:
                trc = round((df.at[i, "Ordering cost"]) * (df.at[i, "Demand (kg)"] / eoq) + (eoq / 2) * (unit_cost_dc[j]) * (df.at[i, "Carrying cost"]) + (df.at[i, "Demand (kg)"]) * (unit_cost_dc[j]))
                eoq_dc.append(eoq)
                boq_dc.append(eoq)
                trc_dc.append(trc)
            else:
                if abs(eoq - ranges_dc_df.at[j, "Lower"]) < abs(eoq - ranges_dc_df.at[j, "Upper"]):
                    q = ranges_dc_df.at[j, "Lower"]
                    eoq_dc.append(eoq)
                    boq_dc.append(q)
                    trc = round((df.at[i, "Ordering cost"]) * (df.at[i, "Demand (kg)"] / q) + (q / 2) * (unit_cost_dc[j]) * (df.at[i, "Carrying cost"]) + (df.at[i, "Demand (kg)"]) * (unit_cost_dc[j]))
                    trc_dc.append(trc)
                else:
                    q = ranges_dc_df.at[j, "Upper"]
                    eoq_dc.append(eoq)
                    boq_dc.append(q)
                    trc = round((df.at[i, "Ordering cost"]) * (df.at[i, "Demand (kg)"] / q) + (q / 2) * (unit_cost_dc[j]) * (df.at[i, "Carrying cost"]) + (df.at[i, "Demand (kg)"]) * (unit_cost_dc[j]))
                    trc_dc.append(trc)
        if i==3:
            eoq = round((2 * df.at[i, "Ordering cost"] * df.at[i, "Demand (kg)"]) / (unit_cost_dfn[j] * df.at[i, "Carrying cost"])) ** (1 / 2)
            if ranges_dfn_df.at[j, "Lower"] <= eoq <= ranges_dfn_df.at[j, "Upper"]:
                trc = round((df.at[i, "Ordering cost"]) * (df.at[i, "Demand (kg)"] / eoq) + (eoq / 2) * (unit_cost_dfn[j]) * (df.at[i, "Carrying cost"]) + (df.at[i, "Demand (kg)"]) * (unit_cost_dfn[j]))
                eoq_dfn.append(eoq)
                boq_dfn.append(eoq)
                trc_dfn.append(trc)
            else:
                if abs(eoq - ranges_dfn_df.at[j, "Lower"]) < abs(eoq - ranges_dfn_df.at[j, "Upper"]):
                    q = ranges_dfn_df.at[j, "Lower"]
                    eoq_dfn.append(eoq)
                    boq_dfn.append(q)
                    trc = round((df.at[i, "Ordering cost"]) * (df.at[i, "Demand (kg)"] / q) + (q / 2) * (unit_cost_dfn[j]) * (df.at[i, "Carrying cost"]) + (df.at[i, "Demand (kg)"]) * (unit_cost_dfn[j]))
                    trc_dfn.append(trc)
                else:
                    q = ranges_dfn_df.at[j, "Upper"]
                    eoq_dfn.append(eoq)
                    boq_dfn.append(q)
                    trc = round((df.at[i, "Ordering cost"]) * (df.at[i, "Demand (kg)"] / q) + (q / 2) * (unit_cost_dfn[j]) * (df.at[i, "Carrying cost"]) + (df.at[i, "Demand (kg)"]) * (unit_cost_dfn[j]))
                    trc_dfn.append(trc)


print("COCOA POWDER:")
data_cp={"EOQ":eoq_cp,
         "BOQ":boq_cp,
         "TRC":trc_cp}
df_cp=pd.DataFrame(data_cp)
print(df_cp)
lowest_cp_trc= df_cp['TRC'].min()
boq_cp_trc= round((df_cp[df_cp['TRC'] == lowest_cp_trc]['BOQ'].values).item())
print("The best quantity of Cocoa Powder to order is",boq_cp_trc,"kg, with a total annual cost of INR",lowest_cp_trc,".\n")

print("COCOA BUTTER:")
data_cb={"EOQ":eoq_cb,
         "BOQ":boq_cb,
         "TRC":trc_cb}
df_cb=pd.DataFrame(data_cb)
print(df_cb)
lowest_cb_trc= df_cb['TRC'].min()
boq_cb_trc= round((df_cb[df_cb['TRC'] == lowest_cb_trc]['BOQ'].values).item())
print("The best quantity of Cocoa Butter to order is",boq_cb_trc,"kg, with a total annual cost of INR",lowest_cb_trc,".\n")

print("DARK CHOCOLATE:")
data_dc={"EOQ":eoq_dc,
         "BOQ":boq_dc,
         "TRC":trc_dc}
df_dc=pd.DataFrame(data_dc)
print(df_dc)
lowest_dc_trc= df_dc['TRC'].min()
boq_dc_trc= round((df_dc[df_dc['TRC'] == lowest_dc_trc]['BOQ'].values).item())
print("The best quantity of Dark Chocolate to order is",boq_dc_trc,"kg, with a total annual cost of INR",lowest_dc_trc,".\n")

print("DRY FRUITS AND NUTS:")
data_dfn={"EOQ":eoq_dfn,
         "BOQ":boq_dfn,
         "TRC":trc_dfn}
df_dfn=pd.DataFrame(data_dfn)
print(df_dfn)
lowest_dfn_trc= df_dfn['TRC'].min()
boq_dfn_trc= round((df_dfn[df_dfn['TRC'] == lowest_dfn_trc]['BOQ'].values).item())
print("The best quantity of Dry fruits and Nuts to order is",boq_dfn_trc," kg, with a total annual cost of INR",lowest_dfn_trc,".\n")

total_cost= lowest_cp_trc+lowest_cb_trc+lowest_dc_trc+lowest_dfn_trc
print("The total annual cost of all the primary ingredients is INR",total_cost,".")
savings= df_cp.at[0,"TRC"]+df_cb.at[0,"TRC"]+df_dc.at[0,"TRC"]+df_dfn.at[0,"TRC"]-total_cost
print("The total savings for ordering with discounts is IRN",savings,".")