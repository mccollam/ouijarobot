$fn=64;


difference()
{
    // Outer box:
    square([40, 60]);
    
    // Inner cutout:
    translate([9.5, 9.5])
        square([21, 41]);
    
    // Cord cutout:
    //translate([15.5, 45.5])
    //    square([9, 13]);
    
    // Screw holes:
    translate([15, 5])
        circle(1.5);
    translate([25, 5])
        circle(1.5);
    translate([15, 55])
        circle(1.5);
    translate([25, 55])
        circle(1.5);
}