import bpy

cv = bpy.data.curves['BezierCurve']

print('-------')

for sp in cv.splines:

    #sp = cv.splines[0]
    print('----------------------')

    # spでもOK. curveを取得してsplinesの0にいってそこからいろいろ調べられるみたい。
    print(len(sp.bezier_points)) # print number of points
    
    for id, p in enumerate(sp.bezier_points):
        
        print("id:" + str(id))
        print("co:" + str(p.co)) # print coordinate of first point
        print("handle_left:" + str(p.handle_left)) # ... and its left handle's coordinate
        print("handle_right:" + str(p.handle_right)) # ... as well as the right one)



