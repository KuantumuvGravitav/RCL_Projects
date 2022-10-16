% Problem:
% A merchant has three items on sale, namely a radio for P50, a clock for P30, and a flashlight for P1.
% At the end of the day, he sold a total of 100 of the three items and has taken exactly P1,000 on the total sales.
% How many radios did he sell? (MATLAB solution)

function items = benta(sold, earned)
% sold = 100
% earned = 1000
% difference1 = 900
difference1 = earned - sold;
for r = 1:sold
    c = (difference1 - 49*r)/29;
    if (49*(r) + 29*(c)) == difference1 && (mod(c, 1) == 0)
        radio = r;
        clock = c;
        break
    else
        continue
    end
end
flashlight = earned - (50*(radio) + 30*(clock));
items = [radio, clock, flashlight];
end
