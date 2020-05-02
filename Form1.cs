using IronPython.Hosting;
using Microsoft.Scripting.Hosting;
using System;
using System.Windows.Forms;
namespace webbrowser_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            if (textBox1.Text.Contains("http"))
            {
                label1.Text = "Phishing!";
                label1.BackColor = System.Drawing.Color.Red;
                label1.ForeColor = System.Drawing.Color.Cyan;
                richTextBox1.Text = "SSL not enabled for this web site";
                richTextBox1.Visible = true;

            }
            else if (textBox1.Text.Contains("@"))
            {
                label1.Text = "Phishing!";
                label1.BackColor = System.Drawing.Color.Red;
                label1.ForeColor = System.Drawing.Color.Cyan;
                richTextBox1.Text = "This site contains @ in its link!";
                richTextBox1.Visible = true;
            }
            else if (textBox1.Text.Contains("@"))
            {
                label1.Text = "Phishing!";
                label1.BackColor = System.Drawing.Color.Red;
                label1.ForeColor = System.Drawing.Color.Cyan;
                richTextBox1.Text = "This site contains - in its link!";
                richTextBox1.Visible = true;
            }
            else if (textBox1.Text.Contains(".html"))
            {
                label1.Text = "Phishing!";
                label1.BackColor = System.Drawing.Color.Red;
                label1.ForeColor = System.Drawing.Color.Cyan;
                richTextBox1.Text = "This site may be hosted from local host so be secure!";
                richTextBox1.Visible = true;
            }
            else
            {
                webBrowser1.Navigate(textBox1.Text);
                label1.Text = "Safe";
                label1.ForeColor = System.Drawing.Color.Yellow;
                label1.BackColor = System.Drawing.Color.Green;
                richTextBox1.Visible = false;

            }


        }

        private void button4_Click(object sender, EventArgs e)
        {
            webBrowser1.Navigate("www.Google.com");
            richTextBox1.Visible = false;
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            webBrowser1.GoBack();
        }

        private void button3_Click_1(object sender, EventArgs e)
        {
            webBrowser1.Refresh();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            webBrowser1.GoForward();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }
        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {


        }

        private void webBrowser1_DocumentCompleted(object sender, WebBrowserDocumentCompletedEventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void BEsecure_Click(object sender, EventArgs e)
        {

        }

        private void panel4_Paint(object sender, PaintEventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Minimized;
        }

        private void button7_Click(object sender, EventArgs e)
        {
            if (this.WindowState == FormWindowState.Maximized)
                this.WindowState = FormWindowState.Normal;
            else if (this.WindowState == FormWindowState.Normal)
            {
                this.WindowState = FormWindowState.Maximized;
            }

        }

        private void button8_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void panel3_Paint(object sender, PaintEventArgs e)
        {

        }

        private void panel1_Paint(object sender, PaintEventArgs e)
        {

        }
    }
    

}