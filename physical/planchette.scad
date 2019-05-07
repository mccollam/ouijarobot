$fn=64;

scale(8)
difference()
{
    union()
    {
        hull()
        {
            circle(10);
            translate([10, 25, 0])
                circle(10);
            translate([25, 10, 0])
                circle(10);
        }

        translate([11, 27, 0])
            circle(10);
        translate([27, 11, 0])
            circle(10);
    }
    
    // Viewing window:
    translate([3, 3, 0])
        circle(5);
}