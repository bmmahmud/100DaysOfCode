<?php

class queries extends CI_Model {

    public function getpost() {
        $query = $this->db->get('todo_table');  // Produces: SELECT * FROM mytable
        if ($query->num_rows() > 0) {
            return $query->result();
        }
    }

    public function addPost($data) {
        return $this->db->insert('todo_table', $data);
    }

    public function getSinglePost($id) {
        $query = $this->db->get_where('todo_table', array('id' => $id));
        if ($query->num_rows() > 0) {
            return $query->row();
        }
    }

    public function updatePost($data, $id) {
        return $this->db->where('id', $id)->update('todo_table', $data);
    }

    public function deletePost($id) {
        return $this->db->delete('todo_table', ['id' => $id]);
    }

    public function search($job) {
        $this->db->selecet('*');
        $this->db->from('todo_table');
        $this->db->like('job', $job);
        $query = $this->db->get();
        if ($query->num_row() > 0) {
            return $query->result();
        } else {
            return $query->result();
        }
    }

}

?>