package com.scysco.unitutor.eventos;

import com.scysco.unitutor.gui.VentanaPrincipal;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

// Implemento el ActionListener para el Click y MouseAdapter para el cambio de color
public class ListenerNuevaTutoria extends MouseAdapter implements ActionListener {

  private VentanaPrincipal gui;

  public ListenerNuevaTutoria(VentanaPrincipal gui) {
    this.gui = gui;
  }

  // para hacer aparecer el formulario como pide el caso de estudio
  // Ademas, implemente ActionListener para recibir acción desde pulso tembloroso
  // notase la diferencia con los otros botones que usan mouseClicked.
  @Override
  public void actionPerformed(ActionEvent e) {
    gui.getPnlFormulario().setVisible(true);
    gui.getPnlContenido().revalidate();
    gui.getPnlContenido().repaint();
    gui.getBtnNueva().setEnabled(false);
  }

  // El cambio de color
  @Override
  public void mouseEntered(MouseEvent e) {
    if (gui.getBtnNueva().isEnabled()) {
      gui.getBtnNueva().setBackground(gui.COLOR_RED_LOW);
      gui.getBtnNueva().setForeground(gui.COLOR_RED);
      gui.getBtnNueva().setBorderColor(gui.COLOR_RED);
    }
  }

  @Override
  public void mouseExited(MouseEvent e) {
    if (gui.getBtnNueva().isEnabled()) {
      gui.getBtnNueva().setBackground(Color.WHITE);
      gui.getBtnNueva().setForeground(Color.BLACK);
      gui.getBtnNueva().setBorderColor(gui.COLOR_GREEN);
    }
  }
}
