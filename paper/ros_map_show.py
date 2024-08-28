from datetime import datetime
import cv2
import numpy as np
def time_stamp_transform(time_stamp: int) -> None:
    print(datetime.fromtimestamp(time_stamp))
    
def map_pgm_show(pgm_file_full_path: str) -> None:
    npf = np.fromfile(pgm_file_full_path, np.uint8)
    img = cv2.imdecode(npf, 1)
    cv2.imshow("img_show", img)
    cv2.waitKey(0)

def test_open3d_axis():
    import open3d as o3d
    p = o3d.geometry.PointCloud()
    axis = o3d.geometry.AxisAlignedBoundingBox()
    axis2 = o3d.geometry.TriangleMesh.create_coordinate_frame(
        size=1, origin=[0,0,0])
    box = o3d.geometry.TriangleMesh.create_box()
    # o3d.visualization.draw([p, axis])
    o3d.visualization.draw_geometries([box, axis2])
    pass