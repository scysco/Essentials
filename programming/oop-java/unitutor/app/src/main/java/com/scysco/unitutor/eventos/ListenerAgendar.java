package com.scysco.unitutor.eventos;

import com.scysco.unitutor.gui.VentanaPrincipal;

import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

/*
   Esta seria una de las clases mas relevantes para la actividad y caso de estudio,
   aquí gestiono la validación de longitud de caracteres, y el comportamiento del 
   botón agendar, tras cumplirse los requisitos de su activación, adicionalmente
   limpio los componentes una vez realizada su función, permitiendo probarlo nuevamente
   */
public class ListenerAgendar extends MouseAdapter {

  private VentanaPrincipal gui;

  public ListenerAgendar(VentanaPrincipal gui) {
    this.gui = gui;
  }

  // Lógica de validación para la longitud minima de 50 caracteres, al final 
  // nos regresara True o False según se hayan cumplido las condiciones
  private boolean esFormularioValido() {
    String nombre = gui.getTxtNombre().getText().trim(); // con trim ignoro espacios al inicio y el final
    String motivo = gui.getTxtMotivo().getText().trim();
    return !nombre.isEmpty() && motivo.length() >= 50; // si nombre NO esta vació Y motivo tiene 50 o mas caracteres
  }

  // Sin relevancia para la actividad, esta es una implementación extra, que permite
  // al usuario saber de manera visual cuando ha cumplido con los 50 caracteres.
  // hago uso de JOptionPane.showMessageDialog() para no crear una nueva ventana desde cero
  public void validarMotivoIndividual() {
    String texto = gui.getTxtMotivo().getText().trim();
    if (texto.length() < 50) {
      JOptionPane.showMessageDialog(gui,
          "El motivo es muy corto (" + texto.length() + "/50).",
          "Validacion", JOptionPane.WARNING_MESSAGE);
    } else {
      JOptionPane.showMessageDialog(gui, "Longitud correcta.", "OK", JOptionPane.INFORMATION_MESSAGE);
    }
  }

  // --- Comportamiento de los eventos ---
  @Override
  public void mouseEntered(MouseEvent e) {
    JButton btn = gui.getBtnAgendar();
    if (esFormularioValido()) {
      btn.setBackground(gui.COLOR_RED);
      btn.setForeground(Color.WHITE);
      btn.setCursor(new Cursor(Cursor.HAND_CURSOR));
      btn.setToolTipText("Listo para agendar");
    } else {
      btn.setCursor(new Cursor(Cursor.DEFAULT_CURSOR));
      btn.setToolTipText("Faltan datos (Nombre o Motivo > 50 chars)");
    }
  }

  @Override
  public void mouseExited(MouseEvent e) {
    JButton btn = gui.getBtnAgendar();
    btn.setBackground(new Color(220, 220, 220));
    btn.setForeground(Color.BLACK);
  }

  @Override
  public void mouseClicked(MouseEvent e) {
    // Igualmente usara JOptionPane.showMessageDialog para evitar mas código
    if (esFormularioValido()) {
      JOptionPane.showMessageDialog(gui, "¡Tutoria agendada con exito para "
          + gui.getTxtNombre().getText() + "!");
      limpiarFormulario();
    } else {
      JOptionPane.showMessageDialog(gui,
          "Error: Revisa que tengas nombre y un motivo mayor a 50 caracteres",
          "Datos incompletos", JOptionPane.ERROR_MESSAGE);
    }
  }

  // Acciones extra para limpiar formulario
  private void limpiarFormulario() {
    gui.getTxtNombre().setText("");
    gui.getTxtMotivo().setText("");
    gui.getCmbTipo().setSelectedIndex(0);
    gui.getPnlFormulario().setVisible(false);
    gui.getBtnNueva().setEnabled(true);
    gui.getBtnNueva().setBackground(Color.WHITE);
    gui.getBtnNueva().setForeground(Color.BLACK);
    gui.getBtnNueva().setBorderColor(gui.COLOR_GREEN);
    gui.getPnlContenido().revalidate();
    gui.getPnlContenido().repaint();
  }
}
