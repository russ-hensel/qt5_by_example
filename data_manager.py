#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bad name
make manager for a model with fields

"""

# ---- tof

import string_util
import key_words

# ---- import end

RECORD_NULL         = 0
RECORD_FETCHED      = 1
RECORD_NEW          = 2
RECORD_DELETE       = 3


# --------------------------------
def model_submit_all( model, msg ):
    """
    add a bit of error checking to submitAll()
    ok     = stuffdb_tabbed_sub_window.model_submit_all( model,  "we are here" )

    ok     = stuffdb_tabbed_sub_window.model_submit_all( model,  f"we are here {id = }" )
    """

    # wat_inspector.go(
    #      msg            = "model_submit_all pre-submit",
    #      # inspect_me     = self.people_model,
    #      a_locals       = locals(),
    #      a_globals      = globals(), )


    if model.submitAll():
        print( f"submitAll {msg}")
        ok   = True
    else:
        error = model.lastError()
        error_msg     = f"submitAll error: {msg}"
        print( error_msg )
        print( f"error text: {error.text()}")
        #AppGlobal.logger.error( error_msg )
        ok   = False

    # wat_inspector.go(
    #      msg            = "model_submit_all post-submit",
    #      # inspect_me     = self.people_model,
    #      a_locals       = locals(),
    #      a_globals      = globals(), )

    return ok



# ---------------------------------
class DataManager(   ):
    """
    model with single db record active at a time
    with gui that is list of custom edits
    extract from stuff then put back
    assumes option of key word update
    may emit some signals somehow
    """

    def __init__(self, model ):
        """
        from creator
            self._build_model()
            self.data_manager      = data_manager.DataManager( self.model )
            self.data_manager..next_key_function = some_function( table_name )

        """
        #super().__init__()
        self.model                  = model
            # all set uup with db connect

        self.next_key_function      = None   # should take table_name  self.next_key_function( self.table_name )
            # note needed if key is generated externally
        self.table_name             = model.tableName()

        self.current_id             = None  # None only if we do not have an id

        self.record_state           = RECORD_NULL

        # self.table_name          = "DetailTabBase unknown, please set"

        # key woerd is up there in parent
        self.key_word_table_name    = ""   # set in init of child ??
        self.id_field               = None   # infered below
        self.field_list             = []
        self.key_word_field_list    = []              # list of edits containing key words
            # field need to hold string data
                # can build with gui


            # check that childred do not also implement this
        self.enable_send_topic_update    = False

    # -------------------------------------
    def enable_key_words( self, key_word_table ):
        """
        support for the key word table
        """
        self.key_word_table_name     = key_word_table
        db                      = self.model.database()
        self.key_word_obj       = key_words.KeyWords(  key_word_table,  db )


    # -------------------------------------
    def add_field( self, edit_field, is_key_word = False  ):
        """
        a field on the form and in the record so to speek
        """
        self.field_list.append( edit_field )
        if edit_field.field_name == "id":
            self.id_field  = edit_field

        if is_key_word:
            self.key_word_field_list.append( edit_field )

    # -------------------------------------
    def new_record( self, next_key = None, option = "default" ):
        """new_record
        looks a bit like default new row
        args
            next_key
            option       "default",  see clear_fields for options
                "prior   use prior on edits

        """
        print( f"DataManager new_record    {self.table_name}  ")
        if next_key is None:
            next_key                = self.next_key_function( self.table_name )

        self.clear_fields( option   = option  )
        self.record_state           = RECORD_NEW

        # think we need to use custon_widget
        #self.id_field.setText( str( next_key ) )
        self.id_field.set_data( next_key, "integer" )

        self.current_id             = next_key
        if self.key_word_table_name:
            self.key_word_obj.string_to_old( "" )

        print( "new_record time stuff may be lost ")

        print( "new_record need to fix up the picture tab if any or does document do it ??")

    # ---------------------------
    def select_record( self, id_value  ):
        """
        from russ crud  works
        move to photo_detail and modify
        then promote
        promoted   seems ok to be here
        """
        record   = None
        model    = self.model

                # consider get rid of thirt if
        if id_value:
            #ia_qt.q_sql_query_model( model, "select_record 1" )
            model.setFilter( f"id = {id_value}" )
            model.select()

            #ia_qt.q_sql_query_model( model, "select_record 2" )
            if model.rowCount() > 0:
                record                  = model.record(0)
                self.id_field.setText( str(record.value("id")) )
                self.record_to_field( record )
                #self.textField.setText(record.value("text_data"))
                self.record_state       = RECORD_FETCHED
                self.current_id         = id_value
            else:
                msg    = f"Record not found! {self.tab_name } {id_value = }"
                print( msg )
                #AppGlobal.logger.error( msg )
                #QMessageBox.warning(self, "Select",  msg )
            #ia_qt.q_sql_query_model( model, "select_record 3 ancestor " )
            # model.setFilter("")  # why what happens if we leave alone
                  # comment out here seems to fix history should be ok across all tabs
            #ia_qt.q_sql_query_model( model, "select_record 4  ancestor" )

        # may be more like events plantings....  remove Picture soon ? or keep as special

        # if record:
        #     #rint( "in DetailTabBase, now dowing history probably only place should be done on select look for other calls  ")
        #     self.parent_window.record_to_history_table( record )

        # # if self.pictures_tab:
        # #     self.pictures_tab.select_by_id( id_value )

        # for i_sub_tab in self.sub_tab_list:
        #     if i_sub_tab:
        #         i_sub_tab.select_by_id( id_value )


        if self.key_word_table_name:
            self.key_word_obj.string_to_old(( self.get_kw_string()) )
        # self.send_topic_update()

    # -----------------------------------------
    def update_db( self, ):
        """
        from russ crud was in phototexttab, probably universal
        looks like can promote to ancestor
        """
        if   self.record_state   == RECORD_NULL:
            print( "update_db record null no action, return ")
            return
            # if self.key_word_table_name:
            #     self.key_word_obj.string_to_new(( self.get_kw_string()) )

        elif  self.record_state   == RECORD_NEW:
            self.update_new_record()
            if self.key_word_table_name:
                self.key_word_obj.string_to_new(( self.get_kw_string()) )

        elif  self.record_state   == RECORD_FETCHED:
            self.update_record_fetched()
            if self.key_word_table_name:
                self.key_word_obj.string_to_new(( self.get_kw_string()) )

        elif  self.record_state   == RECORD_DELETE:
            self.delete_record_update()
            if self.key_word_table_name:
                self.key_word_obj.string_to_new( "" )

        else:
            print( f"update_db wtf  {self.record_state = } ")
        if self.key_word_table_name:
            self.key_word_obj.compute_add_delete( self.current_id  )
        #rint( f"update_db record state now:  {self.record_state = } ")
        #rint( "what about other tabs and subtabs")

    # ---------------------------
    def update_record_fetched(self):
        """
        from russ crud  -- copied from PictureTextTab -- now promoted
        what are the fields
        """
        msg    = ( f"update_record_fetched  {self.record_state  = }")
        print( msg )
        #AppGlobal.logger.error( msg )
        # model    = self.detail_text_model
        model    = self.model      # QSqlTableModel(
        if not self.record_state  == RECORD_FETCHED:

            msg   = ( f"update_record_fetched bad state, return  {self.record_state  = }")
            print( msg )
            #AppGlobal.logger.error( msg )
            return

        id_value = self.id_field.text()
        if id_value:
            # why should we need this
            print( "some save commented out ")
            #model.setFilter(f"id = {id_value}")
            #model.select()
            if model.rowCount() > 0:

                # use mapper or field to record

                record = model.record(0)
                self.field_to_record(  record )
                model.setRecord(0, record)

                # # ---- timestamps
                # record.setValue( "add_ts",   self.add_ts_field.text()) # should have already been set
                # record.setValue( "edit_ts",  self.edit_ts_field.text())

                #model.submitAll()
                ok   = model_submit_all( model, f"DetailTabBase.update_record_fetched {id_value =}")
                # msg            = f"update_record_fetched Record ( fetched ) saved! {id_value =} fix error check "
                # rint( msg )
                #QMessageBox.information(self, "Save",  msg )

            #model.setFilter("")  # seems wrong

    # ---------------------------
    def update_new_record( self ):
        """
        from russ crud worked   --- from photo_text -- worked
        photo-detal ng need edit trying worked --- move to ancestor

        """
        print( f"DetailTabBase update_new_record  {self.record_state  = }")
        model   = self.model     # QSqlTableModel(
        if not self.record_state  == RECORD_NEW:
            msg       = ( f"save_new_record bad state, return  {self.record_state  = }")
            print( msg )
            return

        record  = model.record()

        self.field_to_record( record )

        model.insertRecord( model.rowCount(), record )

        record = model.record(0)
        self.field_to_record(  record )
        model.setRecord(0, record)

        ok   = model_submit_all( model, f"DataManager.update_new_record { self.current_id = } ")

        self.record_state    = RECORD_FETCHED
        # msg      =  f"New record saved! { self.current_id = } "
        # rint( msg )
        #QMessageBox.information(self, "Save New", msg )

    # ---------------------------------------
    def validate( self, ):
        """
        validate all input, like accept text
        validations cause exceptions so return is not really required
        """
        is_bad   = False
        for i_field in  self.field_list:
            is_bad    = i_field.validate(   )
            # if is_bad:
            #     break

        # msg     = f"validate do we need sub_tabs now in stuffdb_tabbed... validate.... {is_bad = } "
        # #AppGlobal.logger.info( msg )
        # print( msg )
        #return is_bad

    # -------------------------------------
    def get_kw_string( self,   ):
        """
        get the fields contaning key words
        and concatinate into one string
        self.field_list.append( edit_field )
        """
        print( "get_kw_string" )
        a_str  = " "
        for i_edit in self.key_word_field_list:
            a_str    = a_str + i_edit.get_raw_data()

        print( f"get_kw_string {a_str = }")
        return a_str

    # -------------------------------------
    def delete_all( self,   ):
        """
        delete all under this id   current_id

        """
        print( "in stuffdb tab delete all ")

        model  = self.model

        # Loop through the rows in reverse order and delete them
        for row in range(model.rowCount() - 1, -1, -1 ):
            model.removeRow(row)

        # tehee is no view here we are more like a form that we may need to clear self.view.show()

        if model.submitAll():
            model.select()  # Refresh the model to reflect changes in the view
        else:
            model.database().rollback()  # Rollback if submitAll fails
            print( "DetailTabBase submitAll fail rollback ")

        for i_sub_tab in self.sub_tab_list:
            if i_sub_tab:
                i_sub_tab.delete_all()


    # ------------------------
    def record_to_field(self, record ):
        """
        promoted
        mov data from fetched record into the correct fields
        """
        # ---- code_gen: detail_tab -- _record_to_field -- begin code
        for i_field in  self.field_list:
            i_field.set_data_from_record( record )

        # next might be better in select_record but does that have the record
        print( "need to fix history" )
        #self.parent_window.record_to_history_table( record )

    # ------------------------
    def field_to_record( self, record ):
        """
        move data from the fields to the record
        """
        for i_field in  self.field_list:
            i_field.get_data_for_record( record, self.record_state  )

    # ------------------------
    def clear_fields( self, option ):
        """
        reset_fields or preset field might be better
        add from_prior here
        what it says, read
        what fields, need a bunch of rename here
        clear_fields  clear_fields  -- or is this default
        !! but should users be able to?? may need on add -- this may be defaults
        "default",
                   "prior   use prior on edits

        move option inside control with argument
        """
        if option == "default":
            for i_field in self.field_list:
               # i_field.clear_data( to_prior = to_prior )
               i_field.set_data_to_default(  )

        elif option == "prior":
            for i_field in self.field_list:
                i_field.set_data_to_prior(  )


    def __str__( self ):

        a_str   = ""
        a_str   = ">>>>>>>>>>* DataManager *<<<<<<<<<<<<"
        a_str   = string_util.to_columns( a_str, ["current_id",
                                           f"{self.current_id}" ] )
        a_str   = string_util.to_columns( a_str, ["enable_send_topic_update",
                                           f"{self.enable_send_topic_update}" ] )
        a_str   = string_util.to_columns( a_str, ["field_list",
                                           f"{self.field_list}" ] )
        a_str   = string_util.to_columns( a_str, ["id_field",
                                           f"{self.id_field}" ] )
        a_str   = string_util.to_columns( a_str, ["key_word_field_list",
                                           f"{self.key_word_field_list}" ] )
        a_str   = string_util.to_columns( a_str, ["key_word_table_name",
                                           f"{self.key_word_table_name}" ] )
        a_str   = string_util.to_columns( a_str, ["model",
                                           f"{self.model}" ] )
        a_str   = string_util.to_columns( a_str, ["next_key_function",
                                           f"{self.next_key_function}" ] )
        a_str   = string_util.to_columns( a_str, ["record_state",
                                           f"{self.record_state}" ] )
        a_str   = string_util.to_columns( a_str, ["table_name",
                                           f"{self.table_name}" ] )
        if self.key_word_table_name:

            a_str   = a_str  + str( self.key_word_obj )

        return a_str


# ---- eof