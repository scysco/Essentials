package com.scysco.unitutor;

import com.scysco.unitutor.gui.VentanaPrincipal; // importo mi venta principal
import javax.swing.SwingUtilities;

public class App {

  public static void main(String[] args) {
    // Aquí estoy usando una expresión lambda para un código mas limpio:
    SwingUtilities.invokeLater(() -> {
      new VentanaPrincipal().setVisible(true);
    });

    /* 
     * Esta seria la instrucción sin lambda:
     SwingUtilities.invokeLater(new Runnable() {
     @Override
     public void run() {
     new VentanaPrincipal().setVisible(true);
     }
     }); 
     */
  }
}
