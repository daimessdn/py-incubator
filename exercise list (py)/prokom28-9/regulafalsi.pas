procedure regula_falsi(a,b: real);
{
	Mencari akar f(x) = 0 di dalam selang [a,b] dengan metode regulafalsi
	K.Awal: a dan b adalah ujung-ujung selang sehingga f(a)*f(b) < 0, nila a dan b sudah terdefinisi
	KAkhir: Hampiran akar tercetak di layar
}
const
	epsilon1 = 0.000001;
	epsilon2 = 0.0000001;
begin
	repeat
		c:=b-(f(b)*(b-a)/(f(b)-f(a)));
		if abs(f(c)) < epsilon2 then
			begin
				a:=c;
				b:=c;
			end
		else
			if f(a)*f(c) < 0 then
				b:=c;
			else
				a:=c;
				
	until (ABS(a-b)< epsilon1) or (f(c)) < epsilon2)
	writeln('Hampiran kar = ', x:10:6);
end;