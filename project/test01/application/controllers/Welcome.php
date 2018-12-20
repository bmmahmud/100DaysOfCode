<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Welcome extends CI_Controller {

public function index(){
	$this->load->model('queries');
	$post = $this->queries->getpost();
	
	$this->load->view('welcome_message',['post'=>$post]);
	
}
public function creat(){
	echo'welcome_message';
}

}
