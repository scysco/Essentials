package com.scysco.unitutor.gui;

import com.scysco.unitutor.componentes.BotonRedondeado;
import com.scysco.unitutor.componentes.RoundedBorder;
import com.scysco.unitutor.eventos.*; // Importo todos mis eventos

import javax.swing.*;
import javax.swing.border.EmptyBorder;
import java.awt.*;

public class VentanaPrincipal extends JFrame {

  // Estos son mis componentes
  private JTextField txtNombre;
  private JTextArea txtMotivo;
  private JComboBox<String> cmbTipo;
  private BotonRedondeado btnNueva, btnAgendar;
  private JPanel pnlFormulario, pnlContenido;
  private JLabel btnCerrar;
  private JPanel pnlHeader;

  // Le creo GETTERS a mis componente para que los eventos puedan acceder.
  // NOTA: Podría hacerlos públicos, desde arriba pero eso es una muy mala 
  // practica, y aunque sea solo un ejercicio académico, debemos interiorizar 
  // este tipo de técnicas
  public JTextField getTxtNombre() {return txtNombre;}
  public JTextArea getTxtMotivo() {return txtMotivo;}
  public JComboBox<String> getCmbTipo() {return cmbTipo;}
  public BotonRedondeado getBtnNueva() {return btnNueva;}
  public BotonRedondeado getBtnAgendar() {return btnAgendar;}
  public JPanel getPnlFormulario() {return pnlFormulario;}
  public JPanel getPnlContenido() {return pnlContenido;}

  // Creo mis colores Públicos por si decido cambiar solo modifico aquí, los 
  // nombres que le di tampoco son la mejor practica pero para este punto creo 
  // que hacen mas fácil de entender lo que busco hacer
  public final Color COLOR_GREEN = new Color(32, 89, 72);
  public final Color COLOR_FONDO = new Color(255, 245, 244);
  public final Color COLOR_RED = new Color(140, 51, 64);
  public final Color COLOR_RED_LOW = new Color(248, 227, 230);

  public final int VENTANA_RADIO = 15; // es un valor que uso para la redondees

  public VentanaPrincipal() {
    // A continuación se viene mucho código de diseño, no hace falta 
    // profundizar en el; solo me permite lograr el resultado final de la GUI.
    setUndecorated(true);
    setSize(420, 600);
    setBackground(new Color(0, 0, 0, 0));
    setLocationRelativeTo(null);
    setLayout(new BorderLayout());
    // Con lo siguiente llamare un segmento de código que me configura aspectos 
    // visuales de la interfaz como el color de fondo y la redondees de 
    // la ventana; No es de importancia para la actividad.
    initFondo();
    // Inicializo componentes
    initHeader(); // el panel verde con titulo y la "X" para cerrar
    initBody(); // Aquí están todos los elementos que me pide la actividad

    // --- IMPORTANTE PARA LA ACTIVIDAD ---
    // --- ASIGNACIÓN DE EVENTOS ---
    // NOTA: he separado la lógica de cada evento en clases separadas
    // Botón Nueva Tutoría 
    //(El caso de estudio pide "que al ser presionado muestre un formulario 
    // emergente para registrar la solicitud")
    ListenerNuevaTutoria eventoNueva = new ListenerNuevaTutoria(this);
    btnNueva.addActionListener(eventoNueva); // Click
    btnNueva.addMouseListener(eventoNueva);  // Cambio de color del botón

    // Botón Agendar (Valido y Guardo)
    ListenerAgendar eventoAgendar = new ListenerAgendar(this);
    btnAgendar.addMouseListener(eventoAgendar);

    // Esta es una validación rápida al dar Enter en Motivo
    // Esta opción es limpia y rápida usando lambda, pero tendría que usar JTextField.
    //txtMotivo.addActionListener(e -> eventoAgendar.validarMotivoIndividual());
    // Ademas la Rubrica pide "KeyListener" así que para esta actividad, quedaría:
    txtMotivo.addKeyListener(new java.awt.event.KeyAdapter() {
      @Override
      public void keyPressed(java.awt.event.KeyEvent e) {
        if (e.getKeyCode() == java.awt.event.KeyEvent.VK_ENTER) {
          eventoAgendar.validarMotivoIndividual();
        }
      }
    });

    // Mover Ventana (no lo pide la actividad, pero también es un evento)
    ListenerMoverVentana mover = new ListenerMoverVentana(this);
    pnlHeader.addMouseListener(mover);
    pnlHeader.addMouseMotionListener(mover);

    // Cerrar App (no lo pide la actividad, pero también es un evento)
    btnCerrar.addMouseListener(new ListenerCerrar(btnCerrar));
  }

  // Sin relevancia para el contexto de la actividad (código de GUI)
  private void initFondo() {
    JPanel pnlMaestro = new JPanel(new BorderLayout()) {
      @Override
      protected void paintComponent(Graphics g) {
        Graphics2D g2 = (Graphics2D) g.create();
        g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
        g2.setColor(COLOR_FONDO);
        g2.fillRoundRect(0, 0, getWidth() - 1, getHeight() - 1, VENTANA_RADIO, VENTANA_RADIO);
        g2.setColor(new Color(200, 200, 200));
        g2.setStroke(new BasicStroke(2));
        g2.drawRoundRect(0, 0, getWidth() - 1, getHeight() - 1, VENTANA_RADIO, VENTANA_RADIO);
        g2.dispose();
      }
    };
    pnlMaestro.setOpaque(false);
    add(pnlMaestro, BorderLayout.CENTER);
  }

  // Mas código de diseño, sin relevancia para la actividad (código de GUI)
  private void initHeader() {
    pnlHeader = new JPanel(new GridBagLayout()) {
      @Override
      protected void paintComponent(Graphics g) {
        Graphics2D g2 = (Graphics2D) g.create();
        g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
        g2.setColor(COLOR_GREEN);
        g2.fillRoundRect(0, 0, getWidth(), getHeight() + 50, VENTANA_RADIO, VENTANA_RADIO);
        g2.dispose();
      }
    };
    pnlHeader.setOpaque(false);
    pnlHeader.setPreferredSize(new Dimension(420, 75));
    GridBagConstraints gbc = new GridBagConstraints();
    gbc.fill = GridBagConstraints.BOTH;
    gbc.weighty = 1.0;

    // Titulo
    gbc.gridx = 0;
    gbc.weightx = 1.0;
    JLabel lblTitulo = new JLabel("UniTutor Express", SwingConstants.CENTER);
    lblTitulo.setFont(new Font("Arial", Font.BOLD, 19));
    lblTitulo.setForeground(Color.WHITE);
    lblTitulo.setBorder(new EmptyBorder(10, 0, 0, 0));
    pnlHeader.add(lblTitulo, gbc);

    // Botón Cerrar
    gbc.gridx = 1;
    gbc.weightx = 0;
    btnCerrar = new JLabel("X", SwingConstants.CENTER);
    btnCerrar.setFont(new Font("Arial", Font.BOLD, 18));
    btnCerrar.setForeground(Color.WHITE);
    btnCerrar.setPreferredSize(new Dimension(65, 75));
    btnCerrar.setCursor(new Cursor(Cursor.HAND_CURSOR));
    pnlHeader.add(btnCerrar, gbc);

    // Agrego al layout creado en initFondo, por eso busco por componente.
    ((JPanel) getContentPane().getComponent(0)).add(pnlHeader, BorderLayout.NORTH);
  }

  // Aquí están todos los componentes pedidos por la actividad y el caso de estudio
  private void initBody() {
    JPanel maestro = (JPanel) getContentPane().getComponent(0); // nuevamente busco por componente

    pnlContenido = new JPanel();
    pnlContenido.setLayout(new BoxLayout(pnlContenido, BoxLayout.Y_AXIS));
    pnlContenido.setOpaque(false);
    pnlContenido.setBorder(new EmptyBorder(20, 20, 10, 40));

    JPanel pnlCentradorBoton = new JPanel(new FlowLayout(FlowLayout.CENTER));
    pnlCentradorBoton.setOpaque(false);
    pnlCentradorBoton.setAlignmentX(0.0f);

    btnNueva = new BotonRedondeado("Nueva tutoria", 15, COLOR_GREEN);
    btnNueva.setPreferredSize(new Dimension(180, 45));
    btnNueva.setBackground(Color.WHITE);
    btnNueva.setForeground(Color.BLACK);
    btnNueva.setFont(new Font("Arial", Font.BOLD, 14));
    pnlCentradorBoton.add(btnNueva);
    pnlContenido.add(pnlCentradorBoton);
    pnlContenido.add(Box.createVerticalStrut(15));

    // Formulario
    pnlFormulario = new JPanel();
    pnlFormulario.setLayout(new BoxLayout(pnlFormulario, BoxLayout.Y_AXIS));
    pnlFormulario.setOpaque(false);
    pnlFormulario.setAlignmentX(0.0f);
    pnlFormulario.setVisible(false);

    JLabel lblSeccion = new JLabel("Nueva tutoria");
    lblSeccion.setFont(new Font("Arial", Font.BOLD, 22));
    lblSeccion.setForeground(COLOR_RED);
    lblSeccion.setAlignmentX(0.0f);
    pnlFormulario.add(lblSeccion);
    pnlFormulario.add(Box.createVerticalStrut(20));

    pnlFormulario.add(crearBloque("NOMBRE DEL ESTUDIANTE", txtNombre = new JTextField()));
    pnlFormulario.add(Box.createVerticalStrut(15));
    pnlFormulario.add(crearBloque("MOTIVO DE LA TUTORIA (Presiona ENTER al terminar)", txtMotivo = new JTextArea(10, 10)));
    pnlFormulario.add(Box.createVerticalStrut(15));

    JLabel lblTipo = new JLabel("TIPO DE TUTORIA");
    lblTipo.setFont(new Font("Arial", Font.BOLD, 11));
    lblTipo.setForeground(new Color(100, 100, 100));
    lblTipo.setAlignmentX(0.0f);
    pnlFormulario.add(lblTipo);
    pnlFormulario.add(Box.createVerticalStrut(8));

    cmbTipo = new JComboBox<>(new String[]{"Regularizacion", "Proyecto", "Examen"});
    cmbTipo.setPreferredSize(new Dimension(Integer.MAX_VALUE, 32));
    cmbTipo.setMaximumSize(new Dimension(Integer.MAX_VALUE, 32));
    cmbTipo.setBackground(Color.WHITE);
    cmbTipo.setAlignmentX(0.0f);
    pnlFormulario.add(cmbTipo);

    pnlContenido.add(pnlFormulario);
    pnlContenido.add(Box.createVerticalGlue());

    maestro.add(pnlContenido, BorderLayout.CENTER);

    // Footer
    btnAgendar = new BotonRedondeado("AGENDAR", 20, COLOR_GREEN);
    btnAgendar.setPreferredSize(new Dimension(150, 50));
    btnAgendar.setBackground(new Color(220, 220, 220));
    btnAgendar.setForeground(Color.BLACK);
    btnAgendar.setFont(new Font("Arial", Font.BOLD, 13));

    JPanel pnlFooter = new JPanel(new FlowLayout(FlowLayout.RIGHT, 0, 0));
    pnlFooter.setOpaque(false);
    pnlFooter.setBorder(new EmptyBorder(0, 0, 45, 45));
    pnlFooter.add(btnAgendar);

    maestro.add(pnlFooter, BorderLayout.SOUTH);
  }

  // Este segmento me ayuda a crear partes del formulario sin repetir tantas 
  // veces el mismo código, recibe un String y un JComponent porque así puedo 
  // recibir tanto un JTextField como un JTextArea ya que heredan de X Component.
  // igual lo que pasa aquí es irrelevante para el tema de la actividad.
  private JPanel crearBloque(String titulo, JComponent field) {
    JPanel p = new JPanel();
    p.setLayout(new BoxLayout(p, BoxLayout.Y_AXIS));
    p.setOpaque(false);
    p.setAlignmentX(0.0f);
    JLabel lbl = new JLabel(titulo);
    lbl.setFont(new Font("Arial", Font.BOLD, 11));
    lbl.setForeground(COLOR_GREEN);
    lbl.setAlignmentX(0.0f);
    field.setPreferredSize(new Dimension(Integer.MAX_VALUE, 32));
    field.setMaximumSize(new Dimension(Integer.MAX_VALUE, 32));
    field.setBorder(BorderFactory.createCompoundBorder(
          new RoundedBorder(12, COLOR_GREEN),
          new EmptyBorder(0, 15, 0, 15)
          ));
    field.setBackground(Color.WHITE);
    field.setAlignmentX(0.0f);
    p.add(lbl);
    p.add(Box.createVerticalStrut(5));
    p.add(field);
    return p;
  }
}
