procedure Newton_Raphson(x:real);

const
	epsilon = 0.0000001;
var
	x_sebelumnya: real;

	function f(x:real):real;

	function f_aksen(x:real):real

begin
	repeat
		x_sebelumnya = x;
		x:= x - f(x)/f_aksen(x);
	until (ABS(x-x_sebelumnya) < epsilon)

	write("Hampiran akar x = ", x:10:6);
end;