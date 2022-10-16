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