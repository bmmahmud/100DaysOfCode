<?php 
class queries extends CI_Model{
   
   public function getpost(){
    $query = $this->db->get('post_table');  // Produces: SELECT * FROM mytable
    if($query->num_rows()>0)
      {
        return $query->result();
      }
}
}
?>