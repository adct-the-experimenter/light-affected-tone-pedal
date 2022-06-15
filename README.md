# Light-Affected Tone Pedal

This is an analog circuit and pcb for the product Light-Affected Tone pedal designed by Another Dimension Effects.

## Simulation
- Web Demo: adfxz.com/light-affected-tone-pedal
- Circuit: light-tone-pedal-circuit.asc


The Light Dependent Resistors used range from 3k ohms to 11k ohms.

## Key Components

- The dual op-amp used is LM358AP.

- Advanced Photonix PDV-8001 LDR https://www.digikey.com/product-detail/en/advanced-photonix/PDV-P8001/PDV-P8001-ND/480602

## Why PWM should not be used

The light-dependent resistor is very sensitive to big changes in light. 
It will pick up the LED turning on and off very quickly and produce high frequency noise close to the flashing frequency of the LED.
Low-pass filter is recommended for use with PWM signals.

## What you can do with the circuit
You are free to copy, modify, sell, or use this circuit in derived works as long as you include the conditions of the license 
and copyright notice with the product. 

If you are selling a product using this circuit or a modified version of it, 
you must include a slip of paper that contains the license conditions and copyright to Another Dimension Effects and Pablo Antinio Camacho Jr.

Read License.txt for details.

##Important Note
Do not place the light dependent resistor or LED(light-emitting diode) on the board.
Instead place the components in a separate board and and connect the leads/terminals to the pcb.

## Warning

Do not mass produce and sell this pedal without FCC compliance in the United States of America.
The same restriction applies to other countries with government bodies concerned with regulation of electro-magnetic interference.

Another Dimension Effects and/or Pablo Antonio Camacho Jr. are not liable for any damage caused by this pedal including EMI.

## Sponsors
The completion of the project is being sponsored by PCBWay.

<img src="https://www.adfxz.com/wp-content/uploads/PCBway1_1.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />
