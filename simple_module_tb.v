`timescale 1ns / 1ps

module simple_module_tb;

reg a;
reg b;
wire y;

simple_and_gate uut (
    .a(a),
    .b(b),
    .y(y)
);

initial begin
    // Initialize inputs
    a = 0;
    b = 0;
    #10;
    
    a = 1;
    b = 0;
    #10;
    
    a = 0;
    b = 1;
    #10;
    
    a = 1;
    b = 1;
    #10;
    
    $finish;
end

initial begin
    $monitor("At time %t, a = %b, b = %b, y = %b", $time, a, b, y);
end

endmodule
