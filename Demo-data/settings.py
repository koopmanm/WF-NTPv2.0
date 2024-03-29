### Input
filename = "C:/Users/p265400/Desktop/JBKirkegaard-multiwormtracker-85a540a2a163/N2-2_2019-07-29-133409-0000 - Copy.avi"
start_frame = 0
limit_images_to = 600
fps = 20.0
px_to_mm = 0.04
darkfield = False
stop_after_example_output = False

### Output
save_as = "C:/Users/p265400/Desktop/JBKirkegaard-multiwormtracker-85a540a2a163/Demo-data/"
output_overlayed_images = 0
font_size =  8
fig_size = (20,20)
scale_bar_size = 1.0
scale_bar_thickness = 7

### Z-filtering
use_images = 100
use_around = 5
Z_skip_images = 1

### Thresholding
keep_dead_method = True
std_px = 64
threshold = 9
opening = 1
closing = 3
skeletonize = True
prune_size = 0
do_full_prune = True

### Locating
min_size = 25
max_size = 120
minimum_ecc = 0.9

### Form trajectories
max_dist_move = 10
min_track_length = 50
memory = 5

### Bending statistics
bend_threshold = 2.1
minimum_bends = 0.0

### Velocities
frames_to_estimate_velocity = 49

### Dead worm statistics
maximum_bpm = 0.5
maximum_velocity = 0.1

### Regions
regions = {'': {'y': [377.36787564766882, 145.24352331606269, 105.45077720207291, 536.53886010362726, 891.35751295336809, 1471.6683937823836, 1833.1191709844561, 1756.8497409326426, 1498.1968911917102, 1077.056994818653, 682.44559585492266, 519.95854922279818], 'x': [274.0725388601038, 675.31606217616604, 1205.8860103626944, 1733.1398963730571, 1845.8860103626944, 1696.6632124352332, 1222.4663212435232, 615.62694300518137, 293.96891191709869, 118.21761658031107, 78.424870466321522, 184.53886010362714]}}

### Optimisation tools
lower = 0
upper = 100
use_average = False
cutoff_filter = True
extra_filter = True
Bends_max = 20.0
Speed_max = 0.035
