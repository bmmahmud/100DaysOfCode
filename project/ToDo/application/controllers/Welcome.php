<?php

defined('BASEPATH') OR exit('No direct script access allowed');

class Welcome extends CI_Controller {

    public function index() {
        $this->load->model('queries');
        $post = $this->queries->getpost();

        $this->load->view('welcome_message', ['post' => $post]);
    }

    public function create() {
        $this->load->view('create');
    }

    public function update($id) {
        $this->load->model('queries');
        $post = $this->queries->getSinglePost($id);

        $this->load->view('update', ['post' => $post]);
    }

    public function search() {
        $this->load->model('queries');
        $job = $this->input->post('search');

        if (isset($job) and ! empty($job)) {
            $data['todo_table'] = $this->queries->search($job);
            $this->load->view('welcome_message', $data);
//            print_r($data['todo_table']);
        } else {
            redirect($this->index());
        }
    }

    public function save() {
        $this->form_validation->set_rules('job', 'Job', 'required');
        $this->form_validation->set_rules('description', 'Description', 'required');

        if ($this->form_validation->run()) {
            $data = $this->input->post();
            unset($data['submit']);

            $today = date('Y-m_d');

            $data['created_date'] = $today;


            $this->load->model('queries');
            if ($this->queries->addPost($data)) {
                $this->session->set_flashdata("msg", 'Post Save Successfully');
            } else {
                $this->session->set_flashdata("msg", 'Failed to Save Post');
            }
            return redirect('welcome');
        } else {
            $this->load->view('create');
        }
    }

    public function change($id) {
        $this->form_validation->set_rules('job', 'Job', 'required');
        $this->form_validation->set_rules('description', 'Description', 'required');

        if ($this->form_validation->run()) {
            $data = $this->input->post();
            unset($data['submit']);

            $today = date('Y-m_d');
            $data['created_date'] = $today;

            $this->load->model('queries');
            if ($this->queries->updatePost($data, $id)) {
                $this->session->set_flashdata("msg", 'Post Update Successfully');
            } else {
                $this->session->set_flashdata("msg", 'Failed to Update Post');
            }
            return redirect('welcome');
        } else {
            $this->load->view('create');
        }
    }

    public function delete($id) {
        $this->load->model('queries');
        if ($this->queries->deletePost($id)) {
            $this->session->set_flashdata("msg", 'Post Deleted Successfully');
        } else {
            $this->session->set_flashdata("msg", 'Failed to Deleted Post');
        }
        return redirect('welcome');
    }

}
